# Beautifulsoup
# 다양한 파서 사용 가능(html.parser, lxml...)
# 태그명, name, 속성(아이디, 클래스, 클래스 선택자)를 이용하여 원하는 요소
# 찾기 가능

import requests
from bs4 import BeautifulSoup

# 페이지 요청
r = requests.get("https://news.v.daum.net/v/20210226094625638")

# soup 객체 생성
soup = BeautifulSoup(r.text, "html.parser")

# 확인
# print(soup)

# 이쁘게 출력하기
# print(soup.prettify())

print(soup.head)  # <head>~~</head> 영역에 있는 모든 내용 가져옴
print()
print(soup.body)  # <body>~~</body> 영역에 있는 모든 내용 가져옴
print()
print(soup.title)  # <title>~~</title> 영역에 있는 모든 내용 가져옴
print()
print(soup.title.name)  # title 태그명 가져오기
print()
print(soup.title.string)  # title 태그 사이의 문자 값
print()
print(soup.title.get_text())
