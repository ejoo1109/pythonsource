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

# insert
cursor = conn.cursor()
# %s : 자리만 넣어놓는것 , 모든데이터 허용
sql = """
    insert into users(username, email, phone, website)
    values(%s,%s,%s,%s)
"""

cursor.execute(sql, ("Park", "park@naver.com", "010-1234-1235", "park.com"))
conn.commit()
conn.close()
