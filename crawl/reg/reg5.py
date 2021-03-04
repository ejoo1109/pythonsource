import re
import openpyxl

# 원본 문자열 "python VS java" 일때 VS로 문자열 앞뒤 분리하기

pattern = re.compile(" VS ")  # 또는 pattern = re.compile(" [A-Z]{2} ")
print(pattern.split("python VS java"))

# 주민번호의 - 기호를 * 로 바꿔서 출력하기
# 801210-1011323
print(re.sub("-", "*", "801210-1011323"))
# 또는
# pattern = re.compile(r"-")
# print(pattern.sub("*","801210-1011323")


# data_kr.xlsx 를 읽어서 주민번호 뒷자리를 ******* 로 바꾸어 출력하기
work_book = openpyxl.load_workbook("./crawl/data/data_kr.xlsx")
sheet1 = work_book.active

pattern = re.compile(r"[0-9]{7}")  # 주민번호 뒤 7자리 지정

for each_row in sheet1.rows:
    print(re.sub(pattern, "*******", each_row[1].value))


work_book.close()