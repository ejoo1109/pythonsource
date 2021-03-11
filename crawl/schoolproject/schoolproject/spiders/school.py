import scrapy


class SchoolSpider(scrapy.Spider):
    name = "school"
    allowed_domains = ["www.w3schools.com"]
    start_urls = ["https://www.w3schools.com/"]

    def parse(self, response):
        # 강좌목록
        lectures = response.css("#mySidenav > div > a::text").getall()
        # 링크주소
        links = response.css("#mySidenav > div > a::attr('href')").getall()

        for idx, lecture in enumerate(lectures):
            yield {"title": lectures, "link": links[idx]}
