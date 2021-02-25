# 다음 증권 인기 검색어 가져오기 (ajax 실시간 자료)

import urllib.request as request
from fake_useragent import UserAgent
import json
import csv  # csv파일을 다룰수 있는 라이브러리

userAgent = UserAgent()

# Request Headers에 있는 정보 다 넣을 수 있음
headers = {"user-agent": userAgent.chrome, "referer": "finance.daum.net"}

# 인기 검색어 요청 URL
url = "https://finance.daum.net/api/search/ranks?limit=10"

try:

    request_url = request.Request(url, headers=headers)
    response = request.urlopen(request_url).read().decode("utf-8")
except Exception as e:
    print(e)
else:
    # print(response)

    # json.loads : JSON 포맷데이터를 파이썬 객체로 변환
    rank_json = json.loads(response)["data"]
    # print(rank_json)

    # 데이터 저장을 위한 리스트
    data = []

    # for문 이용하여 출력
    for item in rank_json:
        print(
            "순위 : {}, 금액 : {}, 회사명 : {}".format(
                item["rank"], item["tradePrice"], item["name"]
            )
        )

        data.append(item)

        with open("c:/finance.txt", "a") as f1, open(
            "c:/finance.csv", "w", newline=""
        ) as f2:
            # txt 저장
            f1.write(
                "순위 : {}, 금액 : {}, 회사명 : {}\n".format(
                    item["rank"], item["tradePrice"], item["name"]
                )
            )

            # csv 저장
            output = csv.writer(f2)
            output.writerow(data[0].keys())  # header
            for row in data:
                output.writerow(row.values())  # value
