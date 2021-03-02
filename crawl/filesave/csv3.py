import csv  # 파이썬에 기본 csv 라이브러리가 들어있음

# csv : 콤마, 로 구분 되어있는 데이터
with open("./crawl/data/sample1.csv", "r") as f:
    # DictReader: 한 행을 기준으로 딕셔너리 형태로 읽어오기
    reader = csv.DictReader(f)
    next(reader)  # next : 헤더명 제거

    for c in reader:  # for문 이용해 줄 단위로 데이터 추출
        print(c)
        for k, v in c.items():  # 원하는 형태로 출력요청
            print(k, v)
        print()
