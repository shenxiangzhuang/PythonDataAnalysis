import os
import time
import datetime
import pandas as pd


# 获取日期和时间
def get_date_and_time():
    # 获取时间戳
    timestamp = time.time()
    # 将时间戳转化为指定格式的时间
    value = datetime.datetime.fromtimestamp(timestamp)
    date_and_time = value.strftime('%Y-%m-%d %H:%M:%S')

    return date_and_time


# 日志文件操作
def write_to_log(logname='Report.txt', operations=None):
    # 检查是否创建了日志文件
    if logname not in os.listdir():
        with open(logname, 'w') as f:
            # 创建文件
            f.writelines(["My Report  --Created by Shen on ", get_date_and_time()])
            f.write("\n")
            # 写入数据
            f.writelines([get_date_and_time(), ': '])
            f.write(operations)
            f.write("\n")
    else:
        # 已有日志文件的话，就以追加的模式写入记录
        with open(logname, 'a') as f:
            # 追加模式写入数据
            f.writelines([get_date_and_time(), ': '])
            f.write(operations)
            f.write("\n")


if __name__ == '__main__':
    write_to_log(operations="Read data from result.csv")
    df = pd.read_csv('result.csv')

    write_to_log(operations="drop the duplicate data")
    df = df.drop_duplicates()

    '''
    Other operations
    '''
