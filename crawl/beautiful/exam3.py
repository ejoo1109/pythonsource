# https://news.v.daum.net/v/20210226111838232
# select_one으로 가져오기

import requests  # 외부의 사이트 가져오기
from bs4 import BeautifulSoup

s = requests.get("https://news.v.daum.net/v/20210226111838232")

soup = BeautifulSoup(s.text, "html.parser")

# 뉴스 제목 가져오기
news_title = soup.select_one("h3")
print(news_title)
print(news_title.string)

print()
# 기사 작성시간 출력
num_date = soup.select_one("span.num_date")
print(num_date)
print(num_date.string)
print()

# 기사의 첫번째 문단 출력 # (서울=뉴스1) 김정한 기자  형태 그대로 출력하려면 {키:밸류}
paragraph = soup.select_one("p[dmcf-pid='cOeD2HXtps']")
print(paragraph)
print(paragraph.string)
print()

# 기사 작성자 출력
writer = soup.select_one("span.txt_info")
print(writer)
print(writer.string)