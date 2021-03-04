# 네이버의 open API 검색 부분 중 도서 정보 가져오기
# 출력 결과
# 번호, isbn , 제목, 가격, 할인가격

import requests

# postman에 있던 headers 키, 밸류 가져오기
header_params = {
    "X-Naver-Client-id": "XChSxv2fe1rP2E7snuD4",
    "X-Naver-Client-Secret": "SULpKuVFlJ",
}
book_api = "https://openapi.naver.com/v1/search/book.json"

start, num = 1, 1
for idx in range(3):
    # 300개 나오게 하기 display가 100으로 설정되었기 때문에 range(3)으로 설정

    start_num = start + (idx * 100)

    param = {"query": "베르나르 베르베르", "start": start_num, "display": 100}

    res = requests.get(book_api, params=param, headers=header_params)

    data = res.json()  # json -> dict 변환

    for item in data["items"]:
        print(num, item["isbn"], item["title"], item["price"], item["discount"])
        num += 1
