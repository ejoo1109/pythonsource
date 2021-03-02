import csv

list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

# 자동 엔터키 입력되나, newline="" 옵션 가능
with open("./crawl/data/sample3.csv", "w", newline="") as f:
    # 2차원 리스트를 csv로 저장
    wt = csv.writer(f)

    for v in list1:
        wt.writerow(v)  # 파일에 한줄씩 list입력
