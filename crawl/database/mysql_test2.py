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

sql = """
    insert into users(username, email, phone, website)
    values('hong','hong@gmail.com','010-1234-1234','hong.com')
"""

cursor.execute(sql)
conn.commit()
conn.close()
