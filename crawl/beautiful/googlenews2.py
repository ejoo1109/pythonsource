# 구글뉴스(news.google.com)에서 뉴스를 검색하고
# 각 뉴스의 하이퍼링크를 수집하는 뉴스 클리핑 프로그램 구현
# keyword받는 형태로 변경

import requests
from bs4 import BeautifulSoup
from urllib.error import HTTPError

# def : 함수정의
def main(keyword):
    # 요청 q=검색어(사용자 입력)를 받는 반복문
    url = "https://news.google.com/search?q=" + keyword + "&hl=ko&gl=KR&ceid=KR%3Ako"

    try:
        with requests.Session() as s:

            res = s.get(url)

            soup = BeautifulSoup(res.text, "html.parser")
            news_clipping = data_extract(soup)

            for news_section in news_clipping:
                for k, v in news_section.items():
                    print("{} : {}".format(k, v))
                print()

    except HTTPError as e:
        print(e)


# 데이터 추출을 담당하는 함수
def data_extract(soup):
    # 뉴스 섹션 영역 가져오기
    ##yDmH0d > c-wiz:nth-child(25) > div > div.FVeGwb.CVnAc.Haq2Hf.bWfURe > div.ajwQHc.BL5WZb.RELBvb > div > main > c-wiz > div.lBwEZb.BL5WZb.xP6mwf > div:nth-child(1) > div > article
    section = soup.select("div.xrnccd > article")  # soup.select : list로 반환
    # print(section)

    # [{link:'',title:''},{},{},{}] 전체적으론 리스트, 각각 article은 dict구조
    news = []
    news_item = {}
    base_url = "https://news.google.com"

    # 링크, 제목, 내용, 출처, 등록일시
    for item in section:
        # 링크, 제목 추출
        link_title = item.select_one("h3 > a")

        # 링크 주소
        # ./articles/CBMiJmh0dHBzOi8vd3d3LmNpb2tvcmVhLmNvbS9pbnNpZGVyLzM5MTUz0gEA?hl=ko&gl=KR&ceid=K
        # print(link_title["href"])
        # https://news.google.com/articles/CBMiJmh0dHBzOi8vd3d3LmNpb2tvcmVh
        news_item["href"] = base_url + link_title["href"][1:]

        # 제목
        # print(link_title.get_text())
        news_item["title"] = link_title.get_text()

        # 요약 내용 추출
        news_item["contents"] = item.select_one("div > span").get_text()

        # 작성일자, 시간, 작성자를 가지고 있는 영역 가져오기
        report_time_date_writer = item.select_one("div.QmrVtf > div.SVJrMe")
        # 작성자 추출
        news_item["writer"] = report_time_date_writer.select_one("a").get_text()
        # 작성일자와 시간 추출 datetime="2021-02-26T01:54:15Z" T를 기준으로 날짜와 시간을 구별
        report_date_time = report_time_date_writer.select_one("time")

        if report_date_time:  # 날짜가 있는경우 T를 기준으로 날짜와 시간을 구별
            report_date_time = report_date_time["datetime"].split("T")
            news_item["report_date"] = report_date_time[0]
            news_item["report_time"] = report_date_time[1]
        else:  # 날짜가 없는경우
            news_item["report_date"] = ""
            news_item["report_time"] = ""

        # 추출된 뉴스에 대한 정보 추가
        news.append(news_item)
        news_item = {}

    # 확인
    # print(news[:3]) # [0,1,2]만 추출
    return news


# 테스트 코드
if __name__ == "__main__":
    main("python")
