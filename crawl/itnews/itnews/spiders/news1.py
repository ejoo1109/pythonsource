import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

# CrawlSpider : 연속적인 페이지 크롤링 할 때 사용
class News1Spider(CrawlSpider):
    name = "news1"
    allowed_domains = ["news.daum.net"]
    start_urls = ["http://news.daum.net/breakingnews/digital"]

    # LinkExtractor : 링크 추출식(정규식 사용)
    rules = [
        Rule(
            LinkExtractor(allow=r"/breakingnews/digital\?page=\d$"),
            callback="parse_headline",
            follow=True,
        )
    ]

    def parse_start_url(self, response):
        # self.logger.info("parse_start_url {}".format(response.url))
        return self.parse_headline(response)

    def parse_headline(self, response):
        self.logger.info("parse_headline {}".format(response.url))

        # 헤드라인과 본문 가져와서 출력
        news_list = response.css("ul.list_allnews > li > div")

        for news in news_list:
            title = news.css(".tit_thumb > a::text").get()
            content = news.css(".desc_thumb > span::text").get().strip()

        yield {"title": title, "content": content}
