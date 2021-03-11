# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import openpyxl


class AlexaprojectPipeline:
    #     def process_item(self, item, spider):
    #         # 순위가 40위 이하만 출력
    #         if item["rank_num"] < 41:
    #             return item
    #         else:
    #             raise DropItem("40위 이상")

    # 초기화 메소드
    def __init__(self):
        # 엑셀처리선언

        # 객체 생성
        self.workbook = openpyxl.Workbook()
        # 기본 시트 활성화
        self.worksheet = self.workbook.active
        # 너비 조절
        self.worksheet.column_dimensions["A"].width = 10
        self.worksheet.column_dimensions["B"].width = 15
        self.worksheet.column_dimensions["C"].width = 15
        self.worksheet.column_dimensions["D"].width = 20

        # 타이틀 행
        self.worksheet.append(["rank_num", "site_name", "daily_time", "daily_page"])

    def process_item(self, item, spider):
        # 순위가 40위 이하만 출력
        if int(item["rank_num"]) < 41:

            # 엑셀저장
            rank_num = item["rank_num"]
            site_name = item["site_name"]
            daily_time = item["daily_time_site"]
            daily_page = item["daily_page_view"]

            self.worksheet.append([rank_num, site_name, daily_time, daily_page])

            return item
        else:
            raise DropItem("40위 이상")

    # 마지막 1회실행
    def close_spider(self, spider):
        self.workbook.save("./result.xlsx")
        self.workbook.close()