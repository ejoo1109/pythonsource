import scrapy
from ..items import AlexaprojectItem


class AlexaSpider(scrapy.Spider):
    name = "alexa"
    allowed_domains = ["www.alexa.com"]
    start_urls = ["https://www.alexa.com/topsites/"]

    def parse(self, response):

        for site in response.css("div.listings > div.site-listing"):
            #    print(site)
            item = AlexaprojectItem()
            # 순위
            item["rank_num"] = site.css("div.td::text").get()
            # > div.listings.table > div:nth-child(2) > div:nth-child(1)
            # 사이트명
            item["site_name"] = site.css("div.DescriptionCell > p > a::text").get()
            # 머문시간
            item["daily_time_site"] = site.css("div:nth-child(3) > p::text").get()
            # 페이지뷰
            item["daily_page_view"] = site.css("div:nth-child(4) > p::text").get()
            yield item