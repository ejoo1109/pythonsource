import scrapy

# scrapy.Spider: 상속받은
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com/tag/humor"]
    start_urls = ["http://quotes.toscrape.com/tag/humor/"]  # 연습용 사이트
    # allowed_domains : start_url에서 시작하여 allowd 까지만 허용도메인,
    # 기입되지 않으면 읽히지 않음
    # 메소드
    # 파싱 : css 또는 xpath
    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "author": quote.xpath("span/samll/text()").get(),
                "text": quote.css("span.text::text").get(),
            }  # span.text::text - span이 가지고 있는 text
            # a::attr - 속성가져오기
        next_page = response.css("li.next a::attr('href')").get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
        # self.parse - 재귀호출
