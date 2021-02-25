# 다음 쇼핑 best100 정보 가져오기

# https://shoppinghow.kakao.com/siso/p/api/bestRank/dispprodbest?vCateId=GMP&durationDays=30&count=100&_=1614242561449
# product_name만 출력
import requests

url = "https://shoppinghow.kakao.com/siso/p/api/bestRank/dispprodbest?vCateId=GMP&durationDays=30&count=100&_=1614242561449"


with requests.Session() as s:
    r = s.get(url)

    for i, item in enumerate(r.json(), 1):  # 1번부터 순번으로 출력
        if i < 101:
            print(i, item["product_name"])

    # for i, row in r.json():
    #     for k,v in row.items():
    #         print("key : {}, value : {}".format(k,v))
    #     print()