# 엑셀파일을 불러와서 정규식 패턴 확인
import re
import openpyxl

# 엑셀파일 불러오기
work_book = openpyxl.load_workbook("./crawl/data/train.xlsx")

# 현재 활성화된 시트 가져오기
sheet1 = work_book.active

# 패턴정의- 정규식 앞에 r 붙이면 정규식으로 인식
# pattern = re.compile(r" [A-Za-z]+\.")  # [' Mr.'] [' Miss.'] 이런식으로 성별타이틀 찾기

# [' Mr.']만 찾기
pattern = re.compile(r" Mr\.")
# name이 포함되어있는 열 가져오기
for each_row in sheet1.rows:
    if len(pattern.findall(each_row[3].value)) > 0:  # Mr.이 있다면
        if pattern.findall(each_row[3].value)[0].strip() == "Mr.":  # 공백제거후 추출
            print(each_row[3].value)

work_book.close()
