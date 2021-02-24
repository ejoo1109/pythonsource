import urllib.request as request

# 정보를 가져올 url
url = "http://google.com"

# 가져온 정보를 저장할 위치
save_url = "c:/google.html"

try:
    # urlretrieve - 요청하는 url의 정보를 로컬파일로 저장
    file1, header1 = request.urlretrieve(url, save_url)
except Exception as e:
    print(e)
else:
    print(header1)
    print("성공")