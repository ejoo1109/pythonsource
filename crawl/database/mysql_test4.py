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
sql = """
    insert into users(username, email, phone, website)
    values(%s,%s,%s,%s)
"""
userList = (
    ("Kim", "kim@naver.com", "010-3333-1235", "kim.com"),
    ("Cho", "cho@naver.com", "010-1111-1235", "cho.com"),
    ("Lee", "lee@naver.com", "010-2222-1235", "lee.com"),
)
cursor.executemany(sql, userList)
conn.commit()
conn.close()
