# 엑셀 파일생성 후 데이터 + 이미지 저장하기
from openpyxl import Workbook
from openpyxl.drawing.image import Image


# 객체 생성-기본 시트 자동생성됨
excel_file = Workbook()
# 기본 시트 활성화
sheet1 = excel_file.active
sheet1.append(["name", "생년월일", "이미지"])

# 데이터 저장하기
rows = [
    ["홍길동", "801020"],
    ["송혜교", "851115"],
    ["김지원", "860912"],
    ["남주혁", "880705"],
]

for idx, row in enumerate(rows, 2):
    img = Image("./crawl/data/golden.jpg")
    img.width = 30
    img.height = 20
    sheet1.append(row)
    sheet1.add_image(img, "C" + str(idx))  # 이미지 삽입시 add_image(위치)

excel_file.save("./crawl/data/test4.xlsx")  # 저장
