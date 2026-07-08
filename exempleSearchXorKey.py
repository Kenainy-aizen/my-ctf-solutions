import base64
import json
from urllib.parse import unquote 
from urllib.parse import quote

# 1. Cookie récupéré (encodé URL)
cookie_encoded = "EGAgHwQ1IxYYMSQYGSZxTUksPFVHYDEQCC0%2FGBlgaVVIJDURDSQ1VRY%3D"

# 2. Décoder l'URL -> Base64 pur
cookie = unquote(cookie_encoded)
# Maintenant cookie vaut : "EGAgHwQ1IxYYMSQYGSZxTUksPFVHYDEQCC0/GBlgaVVIcmNHW3JjVRY="

# 3. Décodage Base64 -> bytes chiffrés
chiffre = base64.b64decode(cookie)

# 4. Texte clair connu
clair = b'{"showpassword":"no","bgcolor":"#ffffff"}'

# 5. XOR pour retrouver la clé (elle se répète)
key = bytearray()
for i in range(len(chiffre)):
    key.append(chiffre[i] ^ clair[i % len(clair)])

# 6. Affichage de la clé (en bytes)
print(key)  # b'qw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8J'
key1 = bytearray()
key =b'kBSw'
print(key)
clair1 = b'{"showpassword":"yes","bgcolor":"#ffffff"}'
for i in range(len(clair1)):
    key1.append(clair1[i] ^ key[i % len(key)])

print(key1)  # Affiche le texte chiffré pour le nouveau message
key1 = base64.b64encode(key1).decode()
key2 = quote(key1)
print(key2)
