# clien 사이트의 팁과 강좌 게시판의 1~5페이지의 타이틀 가져오기

# 1page : https://www.clien.net/service/board/lecture
# 1page : https://www.clien.net/service/board/lecture?&od=T31&po=0
# 2page : https://www.clien.net/service/board/lecture?&od=T31&po=1
# 3page : https://www.clien.net/service/board/lecture?&od=T31&po=2
# 4page : https://www.clien.net/service/board/lecture?&od=T31&po=3
# 5page : https://www.clien.net/service/board/lecture?&od=T31&po=4

import requests
from bs4 import BeautifulSoup

for page_num in range(5):
    if page_num == 0:  # 1page 요청
        r = requests.get("https://www.clien.net/service/board/lecture")
    else:
        r = requests.get(  # page_num 은 int이기때문에 string으로 형변환
            "https://www.clien.net/service/board/lecture?&od=T31&po=" + str(page_num)
        )
    # 게시판의 타이틀 출력
    # div_content > div.list_content > div:nth-child(6) > div.list_title > a.list_subject > span.subject_fixed
    soup = BeautifulSoup(r.text, "html.parser")

    titles = soup.select("div.list_title > a.list_subject > span.subject_fixed")
    for item in titles:
        print(item.text.strip())
    print()