#!/usr/bin/python3

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "root", "book")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

sql = "SHOW TABLES"
# 使用 execute()  方法执行 SQL 查询
cursor.execute(sql)

# 使用 fetchone() 方法获取单条数据.
results = cursor.fetchall()
for row in results:
    print(row)

# 关闭数据库连接
db.close()
