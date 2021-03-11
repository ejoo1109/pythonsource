import scrapy


class TestSpider(scrapy.Spider):
    name = "test2"  # spider 이름
    # allowed_domains = ["www.naver.com", "www.daum.net", "www.zyte.com"]

    # start_urls = [
    #     "https://www.naver.com/",
    #     "https://www.daum.net",
    #     "https://www.zyte.com/blog/",
    # ]
    # start_urls 대신 사용하는 메소드
    def start_requests(self):
        yield scrapy.Request("https://www.naver.com/", self.parse)
        # self.parse 에 url 넘김 == callback
        yield scrapy.Request("https://www.daum.net", self.parse)
        yield scrapy.Request("https://www.zyte.com/blog/", self.parse)

    def parse(self, response):
        # print(response.url)
        # 로그확인
        self.logger.info("Response URL : {}".format(response.url))
        self.logger.info("Response STATUS : {}".format(response.status))

        if response.url.find("zyte"):
            yield {"sitemap": response.url, "contents": response.text[:1000]}
        elif response.url.find("naver"):
            yield {"sitemap": response.url, "contents": response.text[:1000]}
        elif response.url.find("daum"):
            yield {"sitemap": response.url, "contents": response.text[:1000]}
