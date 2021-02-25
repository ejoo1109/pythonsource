import requests

# 가상의 Json 데이터를 만들어서 테스트 할수 있는 곳 jsonplaceholder
# 받아올 데이터가 json 형태일 때
with requests.Session() as s:
    r = s.get("https://jsonplaceholder.typicode.com/todos/1")  # , stream=True
    print("headers : {}".format(r.headers))
    print("json : {}".format(r.json()))
    print("keys() : {}".format(r.json().keys()))  # key값만 가져올경우
    print("values() : {}".format(r.json().values()))  # value값만 가져올경우
    print("encoding : {}".format(r.encoding))
    print("content : {}".format(r.content))

    # 가져오는 데이터를 출력할경우 2가지 방법
    # r.text : text 형태의 응답
    # r.content : binar 형태의 응답
    # content : b'{\n  "userId": 1,\n
