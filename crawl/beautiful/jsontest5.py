# 네이버 쇼핑으로 검색
import requests
import pprint
import openpyxl  # 엑셀로 저장하기 위한 라이브러리
import re

# 엑셀 저장
excel_file = openpyxl.Workbook()
# 기본 시트 활성화
sheet1 = excel_file.active
# 컬럼 너비 변경
sheet1.column_dimensions["B"].width = 100
sheet1.column_dimensions["C"].width = 60
# 타이틀 행 지정
sheet1.append(['순위','상품명','주소'])
# 시트명 지정
sheet1.title = "top1000"


# postman에 있던 headers 키, 밸류 가져오기
header_params = {
    "X-Naver-Client-id": "XChSxv2fe1rP2E7snuD4",
    "X-Naver-Client-Secret": "SULpKuVFlJ",
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
            # item['title'] 영역에 있는 <b> 태그 제거
            title = re.sub('<.+?>',"",item["title"])

            print(num, title, item["link"])
            sheet1.append([num, title, item["link"]]) #행, 리스트구조로 넣어줘야한다.
    else:
        print("Error code: ", res.status_code)

excel_file.save("./crawl/data/top1000.xlsx")
excel_file.close()