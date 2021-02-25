import requests

s = requests.Session()

# get 방식으로 요청
#r = s.get("http://httpbin.org/get")
data = {
    "name" : 'hong'
}
# post 방식으로 요청
#r = s.post("http://httpbin.org/post",data=data)

# delete 방식으로 요청
#r = s.delete("https://httpbin.org/delete")

# put 방식 요청
r = s.put("http://httpbin.org/put",data=data)

print(r.text)

s.close()