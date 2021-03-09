# SQLite : 내장 데이터 베이스 (응용 프로그램에 넣어서 사용)
# 주로 핸드폰안에 있는 데이터 베이스
import sqlite3
from datetime import datetime

# database - 파일이 없다면 생성, 파일이 있다면 연결
conn = sqlite3.connect("./crawl/database/test.db")

# Cursor 획득 -필수실행(쿼리 실행후 반환되는 결과값을 저장하는 메모리공간)
cursor = conn.cursor()

# sql 실행
# IF NOT EXISTS 테이블이 없다면 생성
# number-> integer
# string -> text
sql = """
    CREATE TABLE IF NOT EXISTS users(id integer primary key, username text,
    email text, website text, regdate text)
"""
cursor.execute(sql)
conn.commit()
conn.close()
