import csv  # 파이썬에 기본 csv 라이브러리가 들어있음

# ,로 되어있지 않은 데이터라서 그대로 출력
with open("./crawl/data/sample2.csv", "r") as f:
    reader = csv.reader(f, delimiter="|")  # delimiter="|" 구분기준 부여
    # ['번호', '이름', '가입일시', '나이'] 제거후 출력
    next(reader)  # next : 헤더명 제거

    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:  # for문 이용해 줄 단위로 데이터 추출
        print(c)
