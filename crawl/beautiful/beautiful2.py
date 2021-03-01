import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

userAgent = UserAgent()
headers = {
    'user-agent': userAgent.chrome
}

r = requests.get(
    "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=100&oid=421&aid=0005189301", headers=headers
)

soup = BeautifulSoup(r.text, "html.parser")

# print(type(soup))  # <class 'bs4.BeautifulSoup'>

# print(soup)

# find() : 제일 처음에 만나는 태그를 가져옴
title = soup.find("h3", id='articleTitle') #id='articleTitle' -조금 더 자세히 가져올때

print(title)
print(title.string)
print(title.get_text())
