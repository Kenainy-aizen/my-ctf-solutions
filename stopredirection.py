import requests
from requests.auth import HTTPBasicAuth
url = 'http://localhost/'
auth=('password','username')

response = requests.get(url, auth=auth, params={"revelio": ""}, allow_redirects=False)
print(response.text)
