# SQLite : 내장 데이터 베이스 (응용 프로그램에 넣어서 사용)
# 주로 핸드폰안에 있는 데이터 베이스
# DB Brower for SQLite 설치후 확인
import sqlite3
from datetime import datetime

# sqlite 버전 확인
print("sqlite.version : {}".format(sqlite3.version))

# 날짜랑 시간 생성
now = datetime.now()
print(now)  # 2021-03-09 11:04:53.749413

# 날짜를 원하는 대로 형식 바꾸기
nowDateTime = now.strftime("%Y-%m-%d %H:%M:%S")  # 2021-03-09 11:07:07 월 :m 시간 : M
print(nowDateTime)
