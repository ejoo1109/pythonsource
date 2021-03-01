# gmarket.co.kr 1차 카테고리 명 추출 = find_all()

import requests  # 외부의 사이트 가져오기
from bs4 import BeautifulSoup

s = requests.get("https://gmarket.co.kr")

soup = BeautifulSoup(s.text, "html.parser")

categorys = soup.find_all("span",class_="link__1depth-item")

for category in categorys:
    print(category)
    print(category.string)

# 2차 카테고리 추출
print("\n ----2차 카테고리")
two_categorys = soup.find_all("a",class_="link__2depth-item")
for category in two_categorys:
    print(category)