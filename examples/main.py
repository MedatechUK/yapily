import json
import sys

from http.client import HTTPSConnection
from base64 import b64encode
from types import SimpleNamespace

appuid = ''
appsec = ''

with open('yapily-api-credentials_Aerospace.json', "r") as f:
    config = json.loads(f.read(), object_hook=lambda d: SimpleNamespace(**d))
    for p, v in vars(config).items():
        if p == 'application-uuid':
            appuid = v
        elif p == 'application-secret':
            appsec = v

c = HTTPSConnection("api.yapily.com")
headers = { 'Authorization' : 'Basic %s' %  b64encode(bytearray(appuid + ":" + appsec,'ascii')).decode("ascii") , 'Content-Type': 'application/json',  'Accept' : 'application/json;charset=UTF-8'}
data = {    
    'authCode':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJJTlNUSVRVVElPTiI6Im1vZGVsby1zYW5kYm94IiwiQ09OU0VOVCI6ImUzYWFmMDU5LWU2YTgtNDFhMi04YzAwLTFhYTczODVkZDAzMCIsIkFQUExJQ0FUSU9OX1VTRVJfSUQiOiJweXRob24tc2RrQHlhcGlseS5jb20iLCJVU0VSIjoiYzEwMTQ4MjYtYTIzZi00NzE3LWJiOWEtZTk5MjcxMmYyZWQ5In0.4KY1QNK1ZVxiukIC2VT7LiRI_9ibJliud8V2GwANf3ZdX4duljhOfsan-5Nq6_H6QW_3Ta1RNGcRD5s7Odf_sw', 
    'authState' : 'afcbf8a755844cce92cac62586e5f838'
    }
c.request('POST', '/consent-auth-code',body=json.dumps(data), headers=headers)
res = c.getresponse()
data = res.read()  
print(data)
