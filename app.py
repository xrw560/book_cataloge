from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)
book_dict = {'4k': '四库全书', 'x4k': "续修四库全书"}


@app.route('/')
def index():
    # return "阿娇，我爱你！！！"
    return render_template("love.html")


@app.route('/book', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        param = request.form.get("param")
        table_names = query_table_name()
        results = []
        for table in table_names:
            result = query(table, param)
            results.append((book_dict.get(table), result))

        return render_template("book.html", books=results, param=param, table_names=table_names)
    else:
        return render_template("book.html", books="", param="", table_names=None)


def query_table_name():
    li = []
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
        li.append(row[0])
    # 关闭数据库连接
    db.close()
    return li


def query(table, title):
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "root", "book")

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    sql = "SELECT * from {} where name like '%%{}%%'".format(table, title)
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute(sql)

    # 使用 fetchone() 方法获取单条数据.
    results = cursor.fetchall()
    # 关闭数据库连接
    db.close()
    return results


if __name__ == '__main__':
    app.run()
