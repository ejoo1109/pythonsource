import scrapy
from scrapy_selenium import SeleniumRequest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# gmarket 베스트 여행 카테고리 a 태그 추출


class Gmarket1Spider(scrapy.Spider):
    name = "gmarket1_t"
    # allowed_domains = ["corners.gmarket.co.kr"]
    start_urls = ["https://corners.gmarket.co.kr/Bestsellers?viewType=G&groupCode=G11"]

    def parse(self, response):
        # url 추출
        urls = response.css(
            "#gBestWrap > div > div:nth-child(5) > div:nth-child(3) > ul > li > a::attr('href')"
        ).getall()

        for url in urls:
            # print("url : {}".format(url))
            # yield scrapy.Request(url, self.parse_url)
            yield SeleniumRequest(
                url=url,
                callback=self.parse_url,
                wait_time=3,
                wait_until=EC.element_to_be_clickable((By.CSS_SELECTOR, "h1.itemtit")),
            )

    def parse_url(self, response):
        # print("parse_url : {}".format(response.url))
        # 상품명
        title = response.css("h1.itemtit::text").get()

        yield {"여행 상품 URL": response.url, "여행 상품명": title}
