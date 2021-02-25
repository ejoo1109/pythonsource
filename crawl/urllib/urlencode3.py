import urllib.request as request
from urllib.parse import urlencode
from urllib.error import URLError

search_url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&"

param = {"query":"영화"}

search_url = search_url + urlencode(param)

try:
    data = request.urlopen(search_url).read().decode("utf-8")
except URLError as e:
    print(e)
else:
    print(data[150000:200000])