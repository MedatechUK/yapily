## Build .exe: pyinstaller --onedir savedconsent.py

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
    accounts = AccountsApi(apiClient).get_accounts_using_get(constants.consent)

    c = HTTPSConnection("api.yapily.com")
    headers = { 
        'Authorization' : 'Basic %s' %  b64encode(bytearray(constants.APPLICATION_ID + ":" + constants.APPLICATION_SECRET,'ascii')).decode("ascii") ,
        'Consent' : '%s' % constants.consent
    }
    c.request('GET', '/accounts/'+ accounts.data[0].id +'/transactions/?limit=1&from=2021-07-01', headers=headers)                        
    
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
        
if __name__ == '__main__':
    main()
