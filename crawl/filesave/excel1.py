import openpyxl  # 엑셀 파일 이용을 위한 라이브러리 별도 설치

excel_file = openpyxl.load_workbook("./crawl/data/sample.xlsx")  # 엑셀파일 읽어오기
print(excel_file)
print(type(excel_file))
print(excel_file.sheetnames)  # 시트명 출력

sheet1 = excel_file["영업사원매출"]

for item in sheet1.rows:  # 한행씩 컬럼별 가져오기
    print(
        item[0].value,
        item[1].value,
        item[2].value,
        item[3].value,
        item[4].value,
        item[5].value,
        item[6].value,
    )
