# 방법 1. 기본 라이브러리 이용 json, 방법 2. requests 사용
import requests
import pprint

# postman에 있던 주소가져오기
naver_open_news_api = (
    "https://openapi.naver.com/v1/search/news.json?query=아이폰&sort=sim&display=20"
)

# postman에 있던 headers 키, 밸류 가져오기
header_params = {
    "X-Naver-Client-id": "",
    "X-Naver-Client-Secret": "",
}

res = requests.get(naver_open_news_api, headers=header_params)

if res.status_code == 200:
    # print(res.json()) #json.loads()와 같은 개념
    # pprint.pprint(res.json()) #정리된 형태로 출력함
    data = res.json()
    # print(data["items"][0])  # 첫번째 기사만 출력
    # print()
    # pprint.pprint(data["items"][0])  # 정리된 형태로 출력함

    for idx, item in enumerate(data["items"], 1):  # 타이틀과 링크만 출력
        print(idx, item["title"], item["link"])
else:
    print("Error code: ", res.status_code)
