# SQLite : 내장 데이터 베이스 (응용 프로그램에 넣어서 사용)
# 주로 핸드폰안에 있는 데이터 베이스
import sqlite3
from datetime import datetime

# database - 파일이 없다면 생성, 파일이 있다면 연결
conn = sqlite3.connect("./crawl/database/test.db")

# 커서획득
cursor = conn.cursor()

# sql = "DELETE FROM users WHERE id=?"
# cursor.execute(sql, (3,))

# 딕셔너리 구조
# sql = "DELETE FROM users WHERE id=:id"
# cursor.execute(sql, {"id": 4})

# .rowcount 삭제를 몇개 했는지 알수 있음
print("users db deleted : ", cursor.execute("DELETE FROM users").rowcount)

for user in cursor.execute("select * from users").fetchall():
    print(user)

conn.commit()
conn.close()