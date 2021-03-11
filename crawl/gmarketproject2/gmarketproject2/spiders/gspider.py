import scrapy
from ..items import Gmarketproject2Item

# gmarket 베스트 ALL 제품명, 판매가 출력- 아이템 사용
class GspiderSpider(scrapy.Spider):
    name = "gspider"
    allowed_domains = ["corners.gmarket.co.kr/Bestsellers"]
    start_urls = ["https://corners.gmarket.co.kr/Bestsellers/"]

    def parse(self, response):
        # gmarket 베스트 ALL 제품명, 판매가 출력
        product_names = response.css(
            "div.best-list ul:not(.plus) > li > a::text"
        ).getall()
        product_prices = response.css(
            "div.best-list > ul:not(.plus) > li div.s-price strong span span::text"
        ).getall()

        for idx, product in enumerate(product_names, 0):
            # print("{}. {}, {}".format(idx, product, product_prices[idx]))

            item = Gmarketproject2Item()
            item["title"] = product
            item["price"] = int(product_prices[idx].replace("원", "").replace(",", ""))
            yield item
