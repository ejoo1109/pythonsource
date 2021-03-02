# 로그인 이후에 확인 할 수 있는 정보 크롤링
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

# 로그인시 보내는 formData
login_info = {
    "redirectUrl": "http://www.danawa.com/",
    "loginMemberType": "general",
    "id": "",
    "isSaveId": "true",
    "password": "!!",
}

headers = {
    "user-agent": UserAgent().chrome,
    # F12->Network -> requestheders에 위치
    "Referer": "https://auth.danawa.com/login?url=http%3A%2F%2Fwww.danawa.com%2F",
}

with requests.Session() as s:
    # Origin: https://auth.danawa.com/login
    res = s.post("https://auth.danawa.com/login", login_info, headers=headers)
    print(res.text)