# 네이버 뉴스 가져오기
# https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=421&aid=0005187618

import urllib.request as request
from urllib.error import HTTPError
from fake_useragent import UserAgent


#url = "https://news.v.daum.net/v/20210224184215396"
url = "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=421&aid=0005187618"

try:

    UserAgent = UserAgent()
#headers 정보입력
    headers = {
        'User-agent': UserAgent.chrome
    }
    request_url = request.Request(url, headers=headers)
    response = request.urlopen(request_url).read().decode("euc-kr")
except HTTPError as e:
    print(e)
else:
    print(request_url.header_items())
    print(response[:3000])
