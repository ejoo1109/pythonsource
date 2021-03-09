# SQLite : 내장 데이터 베이스 (응용 프로그램에 넣어서 사용)
# 주로 핸드폰안에 있는 데이터 베이스
import sqlite3
from datetime import datetime

# database - 파일이 없다면 생성, 파일이 있다면 연결
conn = sqlite3.connect("./crawl/database/test.db")

# 커서획득
cursor = conn.cursor()

# sql 실행 - 조회
# sql = "SELECT * FROM users where id=?"
# cursor.execute(sql,(3,))

# %s - 전달받는 포맷
# param = 4
# sql = "SELECT * FROM users where id=%s"
# cursor.execute(sql % param)

# 딕셔너리 형태
# param = {"id":5}
# sql = "SELECT * FROM users where id = :id"
# cursor.execute(sql, param)

# 숫자 선택
param = (3, 5)
sql = "SELECT * FROM users where id IN (?,?)"
cursor.execute(sql, param)

# fetchone(), fetchmany(), fetchall()-커서에 저장된 결과물 가져오기
print("first : ", cursor.fetchone())
print("All : ", cursor.fetchall())


conn.close()