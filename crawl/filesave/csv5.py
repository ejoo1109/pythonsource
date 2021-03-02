import csv

list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

# 자동 엔터키 입력되나, newline="" 옵션 가능
with open("./crawl/data/sample4.csv", "w", newline="") as f:
    # 2차원 리스트를 csv로 저장
    wt = csv.writer(f)

    wt.writerows(list1)
    # 파일에 한줄씩 list입력 writerows: for 문 안쓰고 사용가능
