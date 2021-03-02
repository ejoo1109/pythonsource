# clien 사이트의 자료실 게시판의 타이틀, 작성자, 작성시간 가져오기
# 크롤링한 결과를 엑셀에 저장하기
import requests
from bs4 import BeautifulSoup
import xlsx_write as excel  # 엑셀 저장하는 함수 불러올때
from urllib.error import HTTPError

try:
    with requests.Session() as s:

        r = s.get("https://www.clien.net/service/board/pds")

        soup = BeautifulSoup(r.text, "html.parser")

        # 자료실 담을 리스트 생성
        pds_lists = list()  # psd_lists=[]

        # 테이블 전체 rows 영역 가져오기
        # div_content > div.list_content > div

        rows = soup.select("div.list_content > div")
        # print(rows)

        for row in rows:
            # 타이틀가져오기
            title = row.select_one(
                "div.list_title > a > span.subject_fixed"
            ).string.strip()
            #print(title)
            # 작성자 가져오기 - 2가지 형태(텍스트로 되어있거나 이미지로 되어있음)
            author = row.select_one("div.list_author > span.nickname")

            if author.find("span"):
                author = author.find("span").get_text()
            else:
                author = author.find("img")["alt"] # alt: 이미지가 안나올 경우 글씨로 표시되는 것
            #print(author)

            # 시간 가져오기 : 2021-02-21 16:32:08
            # div_content > div.list_content > div:nth-child(1) > div.list_time > span > span
            date_time = row.select_one("div.list_time > span > span").get_text()
            date_time = date_time.split()[0]
            #print(time)

            pds_lists.append([title,author,date_time])


except HTTPError as e:
    print(e)
else:
    excel.write_excel_template("clien2.xlsx","자료실",pds_lists)
