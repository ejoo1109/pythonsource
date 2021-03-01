# https://finance.naver.com/ 해외증시 이름과 가격 출력

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
    # #container > div.aside > div.group_aside > div.aside_area.aside_stock > table > tbody > tr

    #
    stocks = soup.select(
        #   ".aside_stock table tbody tr "
        # "div.group_aside  div.aside_area.aside_stock  table  tbody  tr"
        "div.group_aside > div.aside_area.aside_stock > table > tbody > tr"
    )
    # print(stocks)
    print(stocks)
    for stock in stocks:
        stock_name = stock.select_one("th > a")
        stock_index1 = stock.find("td")
        print("***")
        print(stock_name.string, stock_index1.string)
