import pymysql  # mysql 과 연동

# database 연결
conn = pymysql.connect(
    host="localhost",
    port=3306,
    user="biguser1",
    password="12345",
    db="bigdata",
    charset="utf8",
)

# print(conn)

# 테이블 생성
cursor = conn.cursor()
# timestamp : 날짜와 시간 == sysdate
# AUTO_INCREMENT(자동증가) == 시퀀스
sql = """
    CREATE TABLE IF NOT EXISTS users(
        id int(11) NOT NULL AUTO_INCREMENT,
        username varchar(20),
        email varchar(100),
        phone varchar(100),
        website varchar(100),
        regdate timestamp DEFAULT CURRENT_TIMESTAMP, 
        PRIMARY KEY(id)
    )
"""

cursor.execute(sql)
conn.commit()
conn.close()
