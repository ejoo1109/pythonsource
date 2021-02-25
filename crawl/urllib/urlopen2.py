import urllib.request as request
from urllib.error import HTTPError

try:
    url = "https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&xfrom=main^gnb"

    response = request.urlopen(url)
    contents = response.read().decode("euc-kr")  # 사이트마다 content 타입이 다를 수 있음
except HTTPError as e:
    print(e)
else:
    print("header info - {}".format(response.info()))
    print("content {}".format(contents[:3000]))  # 3000까지만 추출

# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb9 in position 141: invalid start byte
