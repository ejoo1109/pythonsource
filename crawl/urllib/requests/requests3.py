import requests

# 쿠키값을 같이 전송해야할 때 cookies={"key":"value"}
s = requests.Session()

r = s.get("https://httpbin.org/cookies", cookies={"name": "hong"})

print(r.text)

s.close()