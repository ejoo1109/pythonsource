# 엑셀파일로 저장하는 함수
from openpyxl import Workbook

# filename : 저장될 파일명
# sheetname : 시트이름
# listdata : 저장될 데이터
def write_excel_template(filename, sheetname, listdata):
    # 객체 생성
    excel_file = Workbook()

    # 생성된 기본 시트(Sheet) 활성화
    excel_sheet = excel_file.active

    # 현재 엑셀 시트의 컬럼 너비 조정
    excel_sheet.column_dimensions["A"].width = 60

    # 시트명 변경
    if excel_sheet.title != "":  # 시트명이 비어있지 않다면 변경
        excel_sheet.title = sheetname

    # 시트에 데이터 붙여넣기
    for row in listdata:
        excel_sheet.append(row)

    # 엑셀 파일 저장
    excel_file.save("./crawl/data/" + filename)

    # 엑셀 파일 닫기
    excel_file.close()


# 테스트 코드
if __name__ == "__main__":
    listdata = [
        ["name", "생년월일"],
        ["홍길동", "801020"],
        ["송혜교", "851115"],
        ["김지원", "860912"],
        ["남주혁", "880705"],
    ]
    write_excel_template("info.xlsx", "정보", listdata)