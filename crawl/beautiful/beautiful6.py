from bs4 import BeautifulSoup

# css 선택자로 추출하기

with open("./crawl/beautiful/story.html", "r") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

# select_one() : css 선택자
b = soup.select_one("p.title > b")  # title의 자식태그 b 한개만 선택
print(b)
print(b.string)
print(b.get_text())
print(b.text)

print()
#id 선택
link1 = soup.select_one("#link1")
print(link1)
print(link1.text)

#select : 결과가 리스트로 반환
print()
link2 = soup.select("p.story > a")
print(link2)

print()
link3 = soup.select("p.story > a:nth-of-type(2)") #2번째 요소 가져오기
print(link3)

print()
link4 = soup.select("p.story") #story 클래스 리스트 형태로 가져오기
print(link4)

print()
for i in link4:
    temp = i.find_all("a") #리스트안의 a태그 가져오기

    if temp:
        for v in temp:
            print("----",v)
            print("----",v.string)
    else:
        print("----",i)
        print("----",i.string)
        