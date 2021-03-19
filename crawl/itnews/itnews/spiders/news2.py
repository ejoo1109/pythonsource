import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import ItnewsItem

# CrawlSpider : 연속적인 페이지 크롤링 할 때 사용
class News1Spider(CrawlSpider):
    name = "news2"
    allowed_domains = ["news.daum.net"]
    start_urls = ["http://news.daum.net/breakingnews/digital"]

    # LinkExtractor : 링크 추출식(정규식 사용)
    rules = [
        Rule(
            LinkExtractor(allow=r"/breakingnews/digital\?page=\d$"),
            callback="parse_parent",
            follow=True,
        )
    ]

    def parse_start_url(self, response):
        # self.logger.info("parse_start_url {}".format(response.url))
        return self.parse_parent(response)

    def parse_parent(self, response):
        self.logger.info("Parent Response URL : {}".format(response.url))

        # 링크 추출
        news_list = response.css("ul.list_allnews > li > div")

        for news in news_list:
            article_url = news.css(".tit_thumb > a::attr('href')").get()
            yield scrapy.Request(
                article_url,
                self.parse_child,
                meta={"parent_link": response.url},
                dont_filter=True,
            )  # Request : 한번 더 링크 클릭, 하고 child 메소드 호출, meta :부모주소를 전달

    def parse_child(self, response):
        self.logger.info(
            "Response From Parent URL {}".format(response.meta["parent_link"])
        )
        self.logger.info("Child URL {}".format(response.url))

        # 상세기사에서 기사제목과 내용을 추출
        headline = response.css("h3.tit_view::text").get()

        contents = response.css("section > p::text").getall()
        contents = "".join(contents).strip()

        # item에 담아서 리턴 (부모주소, 상세기사 주소, 기사제목, 내용)
        item = ItnewsItem()
        item["headline"] = headline
        item["contents"] = contents
        item["parent_link"] = response.meta["parent_link"]
        item["article_link"] = response.url

        yield item
