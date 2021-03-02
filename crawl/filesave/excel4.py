from openpyxl import Workbook

# 엑셀 파일생성 후 데이터 저장하기

# 객체 생성-기본 시트 자동생성됨
excel_file = Workbook()
# 기본 시트 활성화
sheet1 = excel_file.active

# 데이터 저장하기
rows = [
    ["name", "생년월일"],
    ["홍길동", "801020"],
    ["송혜교", "851115"],
    ["김지원", "860912"],
    ["남주혁", "880705"],
]

for row in rows:
    sheet1.append(row)

excel_file.save("./crawl/data/test3.xlsx")  # 저장
