# 멜론 프로젝트 생성 - melonproject
# 스파이더 생성 - melon
# 멜론차트
# 곡 제목, 가수명, 앨범 제목 추출 후 저장
import scrapy
from ..items import MelonprojectItem


class MelonSpider(scrapy.Spider):
    name = "melon"
    allowed_domains = ["www.melon.com/chart/index.htm"]
    start_urls = ["https://www.melon.com/chart/index.htm"]

    def parse(self, response):
        # 곡 제목
        songs = response.css("tbody > tr ")
        idx = 0
        for song in songs:
            # 노래명
            title = song.css(
                "td:nth-child(4) > div > div > div.ellipsis.rank01 > span > a::text"
            ).get()
            # 가수명
            singer = song.css("td:nth-child(4) div.rank02 > a::text").get()
            # 앨범 제목
            album = song.css("td:nth-child(5) div.rank03 > a::text").get()

            idx += 1
            yield {"idx": idx, "title": title, "singer": singer, "album": album}
