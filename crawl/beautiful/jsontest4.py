# 네이버 쇼핑으로 검색
import requests
import pprint

# 1~100개까지 가져오기
# "https://openapi.naver.com/v1/search/shop.json?query=아이폰&display=100&start=1"
# 101~200개까지 가져오기
# "https://openapi.naver.com/v1/search/shop.json?query=아이폰&display=100&start=101"
# 201~300개까지 가져오기
# "https://openapi.naver.com/v1/search/shop.json?query=아이폰&display=100&start=201"


# postman에 있던 headers 키, 밸류 가져오기
header_params = {
    "X-Naver-Client-id": "",
    "X-Naver-Client-Secret": "",
}
shop_api = "https://openapi.naver.com/v1/search/shop.json"

start, num = 1, 0
for idx in range(10):  # 무조건 10번반복

    start_num = start + (idx * 100)

    param = {"query": "아이폰", "start": str(start_num), "display": 100}
    # print(shop_api)
    res = requests.get(shop_api, params=param, headers=header_params)

    if res.status_code == 200:
        data = res.json()
        for item in data["items"]:
            num += 1  # 연달아 번호를 부여하기 위해 num 변수 설정
            print(num, item["title"], item["link"])
    else:
        print("Error code: ", res.status_code)
