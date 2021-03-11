import scrapy


class TestSpider(scrapy.Spider):
    name = "test"  # spider 이름
    # allowed_domains = ["www.naver.com", "www.daum.net", "www.zyte.com"]
    # allowed_domains 도 같이 맞춰서 넣어준다.: 크롤링이 허용된 도메인, 정보를 제공하는 정도
    # www.zyte.com/blog/ 일경우 url을 넘기는 메소드를 실행할때 오류발생
    # start_url : 여러개의 사이트를 방문할 때 start_url에 주소 기입, 순서는 지정못함 = 멀티 도메인

    start_urls = [
        "https://www.naver.com/",
        "https://www.daum.net",
        "https://www.zyte.com/blog/",
    ]

    def parse(self, response):
        print(response.css("head > title::text").get())
