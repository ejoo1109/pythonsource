# SQLite : 내장 데이터 베이스 (응용 프로그램에 넣어서 사용)
# 주로 핸드폰안에 있는 데이터 베이스
import sqlite3
from datetime import datetime

# database - 파일이 없다면 생성, 파일이 있다면 연결
conn = sqlite3.connect("./crawl/database/test.db")

# 커서획득
cursor = conn.cursor()

now = datetime.now()
nowDateTime = now.strftime("%Y-%m-%d %H:%M:%S")

# sql 실행- 여러 데이터를 넣을 경우 : executemany
userList = (
    (3, "hong", "hong@naver.com", "hong.com", nowDateTime),
    (4, "cho", "cho@naver.com", "cho.com", nowDateTime),
    (5, "yoo", "yoo@naver.com", "yoo.com", nowDateTime),
)

sql = "INSERT INTO users VALUES(?,?,?,?,?)"

cursor.executemany(sql, userList)  # ? 는 ((튜플))형태로 넣어줘야함
conn.commit()
conn.close()