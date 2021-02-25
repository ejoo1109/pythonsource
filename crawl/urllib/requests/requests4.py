import requests
from fake_useragent import UserAgent

# headers 를 전송해야 할 때
s = requests.Session()

userAgent = UserAgent()

headers = {'user-agent':userAgent.chrome}

r = s.get("https://httpbin.org/get", headers=headers)

print(r.text)

s.close()