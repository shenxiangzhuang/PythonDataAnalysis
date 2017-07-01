import pandas as pd
import pymysql

data = pd.read_csv('result.csv')
rows_num = data.shape[0]

# 创建连接
db = pymysql.connect(host="localhost", user="root", password="zhengfu5zhengfu", db="PyDataBase", charset='utf8')
# 获取游标，我们用它来执行数据库的操作
cursor = db.cursor()

# 执行sql语句
try:
    # 删除表
    # 在创建新表之前检查是否已经存在此表，若存在则先删除
    cursor.execute("DROP TABLE IF EXISTS DOUBAN_BOOK;")
    # 创建表
    cursor.execute("CREATE TABLE DOUBAN_BOOK("
                   "img_urls VARCHAR (100), "
                   "titles VARCHAR (100),"
                   "ratings VARCHAR (20),"
                   "authors VARCHAR (100),"
                   "details VARCHAR (200));")

    for i in range(rows_num):
        sql = "INSERT INTO DOUBAN_BOOK (img_urls, titles, " \
              "ratings, authors, details)VALUES (%s,%s,%s,%s,%s)"
        cursor.execute(sql, (data.ix[i, :][0], data.ix[i, :][1],
                             data.ix[i, :][2], data.ix[i, :][3], data.ix[i, :][4]))
        db.commit()

    cursor.close()

except:
    print("ERROR!")
    db.rollback()

finally:
    db.close()
