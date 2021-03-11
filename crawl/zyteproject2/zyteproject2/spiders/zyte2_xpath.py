import scrapy


class Zyte2Spider(scrapy.Spider):
    name = "zyte2_xpath"
    allowed_domains = ["www.zyte.com/blog"]
    start_urls = ["http://www.zyte.com/blog/"]

    # def parse(self, response):
    #     # 타이틀 추출하기
    #     title = response.xpath(
    #         "//*[@id='_posts_grid-98-2233']/div[1]/div[1]/div[2]/div/a/text()"
    #     ).extract_first()
    #     # 작성 날짜 추출하기
    #     date = (
    #         response.xpath(
    #             "//*[@id='_posts_grid-98-2233']/div[1]/div[1]/a/div[2]/text()"
    #         )
    #         .extract_first()
    #         .strip()
    #     )
    #     # 링크 추출하기
    #     link = response.xpath(
    #         "//*[@id='_posts_grid-98-2233']/div[1]/div[1]/div[2]/div/a/@href"
    #     ).extract_first()

    #     print(title, date, link)

    def parse(self, response):
        # 현재 페이지의 모든 타이틀 추출
        titles = response.xpath(
            "//*[@id='_posts_grid-98-2233']/div[1]/div/div[2]/div/a/text()"
        ).extract()

        # 현재 페이지의 모든 날짜 추출
        dates = response.xpath(
            "//*[@id='_posts_grid-98-2233']/div[1]/div/a/div[2]/text()"
        ).extract()
        # 현재 페이지의 모든 링크 추출
        links = response.xpath(
            "//*[@id='_posts_grid-98-2233']/div[1]/div/div[2]/div/a/@href"
        ).extract()

        for idx, title in enumerate(titles):
            # print("{} {} {}".format(dates[idx].strip(), title, links[idx]))

            # yield - 리턴개념 : Request, Item, Dictionary, None
            yield {"date": dates[idx].strip(), "title": title, "link": links[idx]}
