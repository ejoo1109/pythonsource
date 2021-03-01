from bs4 import BeautifulSoup

# find()로 원하는 부분만 추출하기

with open("./crawl/beautiful/story.html", "r") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

# find() : 제일 처음 만나는 요소
title = soup.find("title")
print("title {}".format(title))
print("title text {}".format(title.string))
print("title parent {}".format(title.find_parent("head")))

# h1 찾기
h1 = soup.find("h1")
print("h1 {}".format(h1))
print("h1 text {}".format(h1.string))

# p 찾기
# p1 = soup.find("p")
p1 = soup.find("p", class_="title")  # class_ : 클래스명이 title을 찾기
print("p {}".format(p1))
print("p text {}".format(p1.string))

# 두번째 p 찾기
p2 = soup.find("p", class_="story")
print("p {}".format(p2))
print("p text {}".format(p2.get_text()))

# 세번째 p 찾기
p3 = p2.find_next_sibling()
print("p {}".format(p3))
print("p text {}".format(p3.string))

# b찾기
b = soup.find("b")
print("b {}".format(b))
print("b text {}".format(b.string))

# a 찾기 id이용
a1 = soup.find("a", id="link1")
print("a {}".format(a1))
print("a text {}".format(a1.string))

# 두번째 a 찾기
a2 = soup.find("a", id="link2")
print("a {}".format(a2))
print("a text {}".format(a2.string))

# 세번째 a 찾기
a3 = soup.find("a", {"class": "sister", "data-io": "link3"})  # 여러개의 속성값으로 찾기 dict 구조 사용
print("a {}".format(a3))
print("a text {}".format(a3.string))
print("a href {}".format(a3["href"]))  # 링크 가져오기
