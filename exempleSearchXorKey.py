import base64
import json

# 1. Le cookie récupéré
cookie = "ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw="

# 2. Décodage Base64 -> texte chiffré (bytes)
chiffre = base64.b64decode(cookie)

# 3. Texte clair connu (les données par défaut en JSON)
clair = '{"showpassword":"no","bgcolor":"#ffffff"}'.encode()

# 4. XOR pour retrouver la clé
key = bytearray()
for i in range(len(chiffre)):
    key.append(chiffre[i] ^ clair[i % len(clair)])  # on utilise le modulo sur le texte clair car il peut être plus court

# 5. Afficher la clé (en bytes)
print(key)  # affiche b'qw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8J'
# La clé qui se répète est "qw8J"
