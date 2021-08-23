import sys
import json
import odata

import uuid,constants,webbrowser
from yapily import ApiClient
from yapily import Configuration
from yapily import AccountAuthorisationRequest

from yapily import AccountsApi
from yapily import ConsentsApi

from http.client import HTTPSConnection
from base64 import b64encode

def main():

    configuration = Configuration()
    configuration.username = constants.APPLICATION_ID
    configuration.password = constants.APPLICATION_SECRET

    apiClient = ApiClient(configuration)

    ## print("\nUsing user:", constants.APPLICATION_USER_ID)

    accounts_api = AccountsApi(apiClient)
    account_authorisation_request = AccountAuthorisationRequest(
        application_user_id=constants.APPLICATION_USER_ID, 
        institution_id=constants.INSTITUTION_ID,
        callback='',
        one_time_token=''
    )
    ## print(account_authorisation_request)
    ## print(configuration)

    ## Execute the account authorisation request to generate an authorisation url to send the user to the bank
    account_authorisation_response = accounts_api.initiate_account_request_using_post(account_auth_request=account_authorisation_request)

    ## Store the consent id
    consent_id = account_authorisation_response.data.id
        
    ## Send the user to the bank to approve the request to retrieve their financial data
    redirect_url = account_authorisation_response.data.authorisation_url
    webbrowser.open(redirect_url)

    ## Wait for the user to authorise before continuing 
    input("\nPress enter to continue AFTER completing the authorisation!")

    ## Check the status of the consent object that was created using the consent id
    consent = ConsentsApi(apiClient).get_consent_by_id_using_get(consent_id=consent_id)

    if (consent.data.status == 'AUTHORIZED'):
        consent_token = consent.data.consent_token

        accounts = AccountsApi(apiClient).get_accounts_using_get(consent_token)

        c = HTTPSConnection("api.yapily.com")
        headers = { 
            'Authorization' : 'Basic %s' %  b64encode(bytearray(constants.APPLICATION_ID + ":" + constants.APPLICATION_SECRET,'ascii')).decode("ascii") ,
            'Consent' : '%s' % consent_token
        }
        c.request('GET', '/accounts/'+ accounts.data[0].id +'/transactions/?limit=1', headers=headers)                        
        
        l = odata.Load(
            ltype = "TST", ## The loading type identifier
            o = c.getresponse(), ## Object Data
            c = "yapily.config", ## Config File
            ex = {
                'meta',
                'links',
                'transactionInformation'
            } ## excluded namespaces
        )  
        
        l.save('odata.json') ## Save to file
        l.post() ## Post to Priority        
            
    else:
        print("\nThe user did not authorise sharing their financial data!")

if __name__ == '__main__':
    main()
