# SQLite : 내장 데이터 베이스 (응용 프로그램에 넣어서 사용)
# 주로 핸드폰안에 있는 데이터 베이스
import sqlite3
from datetime import datetime

# database - 파일이 없다면 생성, 파일이 있다면 연결
conn = sqlite3.connect("./crawl/database/test.db")

# 커서획득
cursor = conn.cursor()

# sql 실행 - 조회
sql = "SELECT * FROM users"

cursor.execute(sql)

# fetchone(), fetchmany(), fetchall()-커서에 저장된 결과물 가져오기
# print("first : ", cursor.fetchone())
# 한 개의 데이터 가져오기

# print("Three : ", cursor.fetchmany(size=3))
# 이미 가져온 데이터 빼고 3개의 데이터 리스트로 가져오기

# print("All : ", cursor.fetchall())
# 이미 가져온 데이터 빼고 모두 가져오기

# for row in cursor.fetchall():  # for문 사용하여 전체 가져오기
#    print(row)

# fetch 사용하지 않고 바로 조회
for row in cursor.execute("SELECT * FROM users order by id desc"):
    print(row)


conn.close()