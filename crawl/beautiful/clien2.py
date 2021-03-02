# clien 사이트의 팁과 강좌 게시판의 1~5페이지의 타이틀 가져오기
# 크롤링한 결과를 엑셀에 저장하기
import requests
from bs4 import BeautifulSoup
import xlsx_write as excel  # 엑셀 저장하는 함수 불러올때
import regex  # 파이썬 정규식 라이브러리(중간에 특수문자로 오류발생하기 때문에)

# import : 파일명으로 바로 부르고 excel별칭 사용

# 엑셀 파일로 보내려면 리스트 형태로 만들어야함
title_lists = []

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
        # print(item.text.strip())
        title = regex.sub("\x1d", " ", item.text.strip())  # sub: "\x1d" 찾아서 " "로 바꿔줌
        title_lists.append([title])
    # print(title_lists)

excel.write_excel_template("clien.xlsx", "팁과강좌", title_lists)
