# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AlexaprojectItem(scrapy.Item):
    # 순위
    rank_num = scrapy.Field()
    # 사이트명
    site_name = scrapy.Field()
    # 머문시간
    daily_time_site = scrapy.Field()
    # 페이지뷰
    daily_page_view = scrapy.Field()