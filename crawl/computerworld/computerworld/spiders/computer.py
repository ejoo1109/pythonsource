import scrapy


class ComputerSpider(scrapy.Spider):
    name = "computer"
    allowed_domains = ["https://www.computerworld.com"]
    start_urls = ["https://www.computerworld.com/news/"]

    def parse(self, response):
        # 세부기사 링크 가져오기
        links = response.css("div.post-cont > h3 > a::attr('href')").getall()
        # 타이틀 모두 가져오기
        titles = response.css("div.post-cont > h3 > a::text").getall()
        # 이미지 전체 주소 가져오기
        images = response.css(
            "figure.well-img > a > img::attr('data-original')"
        ).getall()
        # 간단 내용 가져오기
        contents = response.css("div.post-cont h4::text").getall()

        # 파일로 저장할 수 있는 코드 추가
        for i, article in enumerate(titles):
            link = links[i]
            title = article
            img_url = images[i]
            content = contents[i]
            yield {"title": title, "link": link, "url": img_url, "content": content}
