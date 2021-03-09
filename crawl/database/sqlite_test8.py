# SQLite : 내장 데이터 베이스 (응용 프로그램에 넣어서 사용)
# 주로 핸드폰안에 있는 데이터 베이스
import sqlite3
from datetime import datetime

# database - 파일이 없다면 생성, 파일이 있다면 연결
conn = sqlite3.connect("./crawl/database/test.db")

# 커서획득
cursor = conn.cursor()

# sql = "UPDATE users SET username = ? WHERE id=?"
# cursor.execute(sql, ('kang',3))

# 딕셔너리 구조
sql = "UPDATE users SET username = :username WHERE id=:id"
cursor.execute(sql, {"username": "hong", "id": 3})

for user in cursor.execute("select * from users").fetchall():
    print(user)


conn.close()