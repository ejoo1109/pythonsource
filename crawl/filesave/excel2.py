from openpyxl import Workbook

# 엑셀 파일 저장하기

# 객체 생성-기본 시트 자동생성됨
excel_file = Workbook()
# 기본 시트 이름 확인
print(excel_file.sheetnames)

excel_file.save("./crawl/data/test1.xlsx")  # 저장
