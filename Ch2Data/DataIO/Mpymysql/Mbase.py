import pymysql

# 创建连接
db = pymysql.connect(host="localhost", user="root", password="密码", db="PyDataBase", charset='utf8')
# 获取游标，我们用它来执行数据库的操作
cursor = db.cursor()


# 　打印列名与列定义
def print_colnames():
    cursor.execute("SHOW COLUMNS FROM Py_Create;")
    col_names = cursor.fetchall()
    print(col_names)
    return col_names


# 查询数据
def pritn_alldata():
    cursor.execute("SELECT * FROM Py_Create;")
    data = cursor.fetchall()  # 获取全部数据
    print("All data: ", data)
    return data


# 执行sql语句
try:
    # 删除表
    # 在创建新表之前检查是否已经存在此表，若存在则先删除
    cursor.execute("DROP TABLE IF EXISTS Py_Create;")
    # 创建表
    cursor.execute("CREATE TABLE Py_Create(username VARCHAR (10), useraddr VARCHAR (20));")
    # 插入数据
    cursor.execute("INSERT INTO Py_Create (username,useraddr) VALUES ('员工一', '中国');")
    cursor.execute("INSERT INTO Py_Create (username,useraddr) VALUES ('员工二', '美国');")

    # 打印数据
    pritn_alldata()

    # 字段与记录的操作

    # 记录操作
    # 插入就是INSERT语句
    # 删除使用where
    cursor.execute("DELETE FROM Py_Create WHERE useraddr='美国'")

    # 打印数据
    pritn_alldata()

    # 字段操作
    # 打印修改前的列
    print_colnames()

    # 删除列
    cursor.execute("ALTER TABLE Py_Create DROP username;")
    # 添加列
    cursor.execute("ALTER TABLE Py_Create ADD COLUMN (age TINYINT UNSIGNED);")

    # 打印修改后的列
    print_colnames()
    # 关闭cursor
    cursor.close()

    # 提交上面的增删表和插入数据的操作到数据库
    db.commit()


except:
    db.rollback()
    print("ERROR!")

finally:
    # 关闭数据库连接
    db.close()
