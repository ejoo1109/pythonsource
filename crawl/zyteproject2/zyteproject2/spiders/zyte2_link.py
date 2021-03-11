import scrapy


class Zyte2Spider(scrapy.Spider):
    name = "zyte2_link"
    allowed_domains = ["www.zyte.com"]
    start_urls = ["https://www.zyte.com/blog/"]

    # def parse(self, response):
    # # 타이틀 추출하기
    # title = response.css(
    #     "#_posts_grid-98-2233 > div.oxy-posts > div:nth-child(1) > div.oxy-post-wrap > a::text"
    # ).get()
    # # 작성 날짜 추출하기
    # date = (
    #     response.css(
    #         "#_posts_grid-98-2233 > div.oxy-posts > a > div.oxy-post-image-date-overlay::text"
    #     )
    #     .get()
    #     .strip()
    # )
    # # 링크 추출하기
    # link = response.css(
    #     "#_posts_grid-98-2233 > div.oxy-posts > div:nth-child(1) > div.oxy-post-wrap > div > a::attr('href')"
    # ).get()

    # print(title, date, link)

    def parse(self, response):

        # 현재 페이지의 모든 링크 추출

        for url in response.css(
            "#_posts_grid-98-2233 > div.oxy-posts > div > div.oxy-post-wrap > div > a::attr('href')"
        ).getall():

            # response.urljoin : 재귀호출시 상대경로로 되어있는 주소를 절대 경로로 변경
            yield scrapy.Request(response.urljoin(url), self.parse_article)
            # scrapy.Request(요청할 url , self.가지고 있는 함수명)

    def parse_article(self, response):
        print(response.url)

        contents = response.css("#blog-body span p::text").extract_first()
        # print(contents)
        yield {"contents": contents}
