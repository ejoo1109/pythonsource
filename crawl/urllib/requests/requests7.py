import requests
#json 데이터가 여러개 오는경우
# 가상의 Json 데이터를 만들어서 테스트 할수 있는 곳 jsonplaceholder
# 받아올 데이터가 json 형태일 때
with requests.Session() as s:
    r = s.get("https://jsonplaceholder.typicode.com/users")  # , stream=True

   # print(r.json())

    for row in r.json():
        for k,v in row.items():
            print("key : {}, value : {}".format(k,v))
        print()