# g마켓 best ALL 전체 카테고리 크롤링
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re
from ..items import GmarketbestItem


class Best1Spider(CrawlSpider):
    name = "best1"
    allowed_domains = ["corners.gmarket.co.kr"]
    start_urls = ["http://corners.gmarket.co.kr/Bestsellers/"]

    rules = [
        Rule(
            LinkExtractor(allow=r"/Bestsellers\?viewType=G&groupCode=G(0|1)\d$"),
            callback="parse_sub_category",
        )
    ]

    def parse_start_url(self, response):
        print(">>>> parse_start_url ", response.url)
        yield scrapy.Request(
            response.url, self.parse_item, meta={"main_cate": "ALL", "sub_cate": "ALL"}
        )

    def parse_sub_category(self, response):

        # 1차 카테고리명 추출
        main_cate = response.css("div.gbest-cate ul li.on a::text").get()
        print("{} {} ".format(main_cate, response.url))

        # 1차 카테고리 best100 상품 출력
        yield scrapy.Request(
            response.url,
            self.parse_item,
            meta={"main_cate": main_cate, "sub_cate": main_cate},
            dont_filter=True,
        )

        # 2차 카테고리 추출 - 관련상품군 제외
        sub_cate_addr = response.css(
            "div.navi ul li[class!='related'] a::attr('href')"
        ).getall()
        sub_cate_name = response.css(
            "div.navi ul li[class!='related'] a::text"
        ).getall()

        for idx, sub_addr in enumerate(sub_cate_addr):
            sub_url = response.urljoin(sub_addr)
            sub_name = sub_cate_name[idx]
        # print("2차 카테고리 ", sub_url, sub_name)

        yield scrapy.Request(
            sub_url,
            self.parse_item,
            meta={"main_cate": main_cate, "sub_cate": sub_name},
            dont_filter=True,
        )

    # 상품을 추출하는 콜백함수
    def parse_item(self, response):
        # print(
        #     "parse_item {}, main_cate {}, sub_cate {}".format(
        #         response.url, response.meta["main_cate"], response.meta["sub_cate"]
        #     )
        # )

        # ALL : 200개 아이템 추출
        # 나머지 : 100개 아이템 추출

        best_list2 = response.css("div.best-list")[1]

        best_list = best_list2.css("ul > li")

        for idx, items in enumerate(best_list, 1):
            # 아이템 코드
            # http://item.gmarket.co.kr/Item?goodscode=1350339365&ver=6375116092840
            href = items.css("a.itemname::attr('href')").get()
            # code=1350339365
            pattern = re.compile("code=[0-9]+")
            # ['code','1350339365']
            item_code = pattern.findall(href)[0].split("=")[1]

            # 제품명
            title = items.css("a.itemname::text").get()
            # 원가격
            ori_price = items.css("div.o-price > span > span::text").get()
            # 판매가격
            dis_price = items.css("div.s-price span span::text").get()
            # 할인율
            discount_percent = items.css("div.s-price > span em::text").get()

            # 원 가격이 없는경우
            if ori_price == None:
                ori_price = dis_price

            # 가격에서 , 와 원 글자 지우기
            ori_price = ori_price.replace("원", "").replace(",", "")
            dis_price = dis_price.replace("원", "").replace(",", "")

            # 할인율이 없는 경우
            if discount_percent == None:
                discount_percent = "0"
            else:
                # % 기호 제거
                discount_percent = discount_percent.replace("%", "")

            # print(
            #     "상품명 {}, 원가격 {}, 판매가격 {}, 할인율 {}".format(
            #         title, ori_price, dis_price, discount_percent
            #     )
            # )
            best_item = GmarketbestItem()
            best_item["ranking"] = idx
            best_item["main_cate"] = response.meta["main_cate"]
            best_item["sub_cate"] = response.meta["sub_cate"]
            best_item["item_code"] = item_code
            best_item["title"] = title
            best_item["ori_price"] = ori_price
            best_item["dis_price"] = dis_price
            best_item["discount_percent"] = discount_percent
            yield best_item
