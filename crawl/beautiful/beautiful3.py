from bs4 import BeautifulSoup

# 태그명으로 원하는 부분만 추출하기

with open("./crawl/beautiful/story.html", "r") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

# print(soup.prettify())

# -----------------------------------------------
# title 태그
print("title >> {}".format(soup.title))
print("title text >> {}".format(soup.title.string))
print("title parent >> {}".format(soup.title.parent))  # title 기준으로 부모속성

# h1태그
print("h1 >> {}".format(soup.h1))
print("h1 text >> {}".format(soup.h1.string))

# -----------------------------------------------
# h2태그
print("h2 >> {}".format(soup.h2))
print("h2 text >> {}".format(soup.h2.string))

# -----------------------------------------------
# 첫번째 p 태그
p1 = soup.p
print("첫번째 p >> {}".format(p1))
print("p text >> {}".format(p1.string))
print("p class name >> {}".format(p1["class"]))  # list 형태로 나옴

# -----------------------------------------------
# 두번째 p 태그
p2 = p1.find_next_sibling("p")  # p1의 다음 형제의 p태그
print("두번째 p >> {}".format(p2))
print(
    "p text >> {}".format(p2.get_text())
)  # string 사용시 a태그가 포함되어있기 때문에 나오지않음 get_text()로 사용
print("p class name >> {}".format(p2["class"]))  # list 형태로 나옴

# -----------------------------------------------
# 세번째 p 태그
p3 = p2.find_next_sibling("p")
print("세번째 p >> {}".format(p3))
print("p text >> {}".format(p3.string))
print("p class name >> {}".format(p3["class"]))

# -----------------------------------------------
# b 태그
b = soup.b
print("b >> {}".format(soup.b))
print("b text >> {}".format(soup.b.string))

# -----------------------------------------------
# 첫번째 a 태그 - 태그, 문자
a = soup.a
print("첫번째 a >> {}".format(a))
print("a text >> {}".format(a.string))
print("a class name >> {}".format(a["class"]))

# -----------------------------------------------
# 두번째 a 태그
a1 = a.find_next_sibling("a")
print("두번째 a >> {}".format(a1))
print("a text >> {}".format(a1.string))
print("a class name >> {}".format(a1["class"]))

# -----------------------------------------------
# 세번째 a 태그
a2 = a1.find_next_sibling("a")
print("세번째 a >> {}".format(a2))
print("a text >> {}".format(a2.string))
print("a class name >> {}".format(a2["class"]))