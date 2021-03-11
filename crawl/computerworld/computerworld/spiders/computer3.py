import scrapy
from ..items import ComputerworldItem

# 아이템 사용 / 상세페이지


class ComputerSpider(scrapy.Spider):
    name = "computer3"
    # allowed_domains = ["https://www.computerworld.com"]
    start_urls = ["https://www.computerworld.com/news/"]

    def parse(self, response):
        # 세부기사 링크 가져오기
        links = response.css("div.post-cont > h3 > a::attr('href')").getall()
        # 타이틀 모두 가져오기
        # titles = response.css("div.post-cont > h3 > a::text").getall()
        # # 이미지 전체 주소 가져오기
        # images = response.css(
        #     "figure.well-img > a > img::attr('data-original')"
        # ).getall()
        # # 간단 내용 가져오기
        # contents = response.css("div.post-cont h4::text").getall()

        # # 파일로 저장할 수 있는 코드 추가
        # for i, article in enumerate(titles):
        #     link = links[i]
        #     title = article
        #     img_url = images[i]
        #     content = contents[i]
        #     yield {"title": title, "link": link, "url": img_url, "content": content}

        # url: /articl/3608956/android-12-little-touches.html 형식인데
        # response.urljoin(url) : https://www.computerworld.com 이 앞에 붙음

        # 아이템으로 저장할 수 있는 코드 추가
        for url in links:
            yield scrapy.Request(
                response.urljoin(url),
                self.parse_article,
                meta={"url": response.urljoin(url)},
            )

    def parse_article(self, response):
        # print(response.url)
        # 상세페이지 조회
        # 타이틀 가져오기
        # title = response.css("h1::text").get()
        # # 이미지 전체 주소 가져오기
        # image = response.css("figure.hero-img > img::attr('data-original')").get()
        # # 간단 내용 가져오기
        # content = response.css("#drr-container > p::text").getall()

        item = ComputerworldItem()

        item["title"] = response.css("h1::text").get()
        item["img_url"] = response.css(
            "figure.hero-img > img::attr('data-original')"
        ).get()
        item["content"] = "".join(response.css("#drr-container > p::text").getall())
        item["link"] = response.meta["url"]

        yield item