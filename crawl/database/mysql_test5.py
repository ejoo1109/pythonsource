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
# ? 처리 불가능=> %s : 자리만 넣어놓는것 , 모든데이터 허용
# sql = """
#     select * from users
# """


sql = """
    select * from users where id = %s
"""

cursor.execute(sql % 4)

print(cursor.fetchone())

# DictCursor-딕셔너리 형태
cursor1 = conn.cursor(pymysql.cursors.DictCursor)
cursor1.execute("select * from users where id IN(%s,%s)" % (3, 5))

for row in cursor1.fetchall():
    print(row["username"])


conn.commit()
conn.close()
