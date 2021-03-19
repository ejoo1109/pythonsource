# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class GmarketbestPipeline:
    def __init__(self):  # DB 커넥션 연결
        self.conn = pymysql.connect(
            host="localhost",
            port=3306,
            user="biguser1",
            passwd="12345",
            database="bigdata",
            charset="utf8",
        )

        if self.conn:
            print("Connection 성공")
        else:
            print("Connection 실패")

        self.cursor = self.conn.cursor()

    def open_spider(self, spider):
        spider.logger.info("GmarketBest Pipeline Started")

        sql = """
            CREATE TABLE IF NOT EXISTS product(
                item_code varchar(20) not null primary key,
                title varchar(200) not null,
                ori_price int not null,
                dis_price int not null,
                discount_percent int not null
            )
        """
        self.cursor.execute(sql)
        # auto_increment : 오라클에서의 시퀀스
        # unsigned : -값을 사용하지 않음, tinyint: 1byte 사용(0~255까지 사용)
        sql = """
            CREATE TABLE IF NOT EXISTS ranking(
                num int auto_increment not null primary key,
                main_category varchar(80) not null,
                sub_category varchar(80) not null,
                item_ranking tinyint unsigned not null,
                item_code varchar(20) not null)
        """
        self.cursor.execute(sql)

    # insert작업
    def process_item(self, item, spider):

        sql = """
            INSERT INTO product(item_code, title, ori_price, dis_price, discount_percent)
            values(%s,%s,%s,%s,%s)
        """
        values = (
            item.get("item_code"),
            item.get("title"),
            item.get("ori_price"),
            item.get("dis_price"),
            item.get("discount_percent"),
        )
        self.cursor.execute(sql, values)

        sql = """
            INSERT INTO ranking(main_category, sub_category, item_ranking, item_code)
            values(%s,%s,%s,%s)
        """
        values = (
            item.get("main_cate"),
            item.get("sub_cate"),
            item.get("ranking"),
            item.get("item_code"),
        )

        self.cursor.execute(sql, values)
        self.conn.commit()

        return item

    def close_spider(self, spider):
        spider.logger.info("GmarketBest Pipeline Stopped")
        self.conn.close()