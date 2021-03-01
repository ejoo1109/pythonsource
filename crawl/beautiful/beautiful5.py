from bs4 import BeautifulSoup

# find_all()로 추출하기 - 찾고자 하는 태그를 모두 찾아서
#                         결과를 무조건 list로 형태로 반환

with open("./crawl/beautiful/story.html", "r") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

# a = soup.find_all("a") # a 태그를 list 형태로 가져오기
a = soup.find_all("a", limit=2)  # limit : 개수 제한
print(a)

link = soup.find_all("a", class_="sister")
print(link)

print()
# string : 텍스트 노드 값을 지정해서 가져올 수 있음
link1 = soup.find_all("a", string=["Elsie"])
print(link1)

print()
link2 = soup.find_all("a", string=["Elsie", "Tillie"])
print(link2)