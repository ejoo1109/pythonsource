# https://finance.naver.com/ 인기검색 종목란의 이름과 가격 출력

import requests
from bs4 import BeautifulSoup
from urllib.error import HTTPError

try:

    url = "https://finance.naver.com/"

    with requests.Session() as s:
        # get(), soup 객체 생성
        s = requests.get(url)
        soup = BeautifulSoup(s.text, "html.parser")
except HTTPError as e:
    print(e)
else:
    # container > div.aside > div.group_aside > div.aside_area.aside_popular > table > tbody > tr
    stocks = soup.select(
        "div.group_aside > div.aside_area.aside_popular > table > tbody > tr"
    )
    # print(stocks)

    for stock in stocks:
        stock_name = stock.select_one("th > a")
        stock_price = stock.find("td")
        print(stock_name.string, stock_price.string)
