import scrapy


class Zyte1Spider(scrapy.Spider):
    name = "zyte1"
    allowed_domains = ["www.zyte.com/blog"]
    start_urls = ["https://www.zyte.com/blog/"]

    def parse(self, response):
        # pass  # pass 추후에 완성시킬 예정일때
        # print(response.text)
        print("response.url : {}".format(response.url))
        print("dir : {}".format(dir(response)))
        print("status : {}".format(response.status))
        print("body : {}".format(response.body))