# 실습 - 다음 뉴스 가져오기
# https://news.v.daum.net/v/20210224184215396

import urllib.request as request
from urllib.error import HTTPError

url = "https://news.v.daum.net/v/20210224184215396"

try:
    response = request.urlopen(url).read().decode("utf-8")
except HTTPError as e:
    print(e)
else:
    print(response)
