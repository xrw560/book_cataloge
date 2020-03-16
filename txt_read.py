def mysql(val):
    import pymysql

    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "root", "book")

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    sql = "INSERT INTO x4k(name,category,author,number) VALUES(%s,%s,%s,%s)"
    # 使用 execute()  方法执行 SQL 查询
    cursor.executemany(sql, val)
    db.commit()
    # 关闭数据库连接
    db.close()


if __name__ == "__main__":
    result = []
    with open('x4k.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            words = line.split("\t")
            category = words[0]
            number = words[1]
            pos = words[2].find('(')
            if pos >= 0:
                author = words[2][pos:].strip()
                name = words[2][:pos]
                print(name, category, author, number)
                result.append((name, category, author, number))
            else:
                print(pos)
    mysql(result)
