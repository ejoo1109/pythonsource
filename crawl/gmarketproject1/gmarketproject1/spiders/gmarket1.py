import scrapy


class Gmarket1Spider(scrapy.Spider):
    name = "gmarket1"
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
            print("{}. {}, {}".format(idx, product, product_prices[idx]))
