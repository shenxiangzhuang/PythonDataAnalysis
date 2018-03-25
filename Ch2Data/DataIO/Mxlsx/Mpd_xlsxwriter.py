'''

pandas 与 xlsxwriter交互[需要安装xlsxwriter]
https://xlsxwriter.readthedocs.io/working_with_pandas.html
'''

import os
import pandas as pd

# 文件夹切换
if 'Myxlsxdata' not in os.listdir():
    os.mkdir('Myxlsxdata')
os.chdir('Myxlsxdata')

# 数据1
books_data = pd.read_csv('result.csv', usecols=['titles', 'authors', 'ratings', 'details'], na_values='NULL')
df1 = pd.DataFrame(books_data)
# 数据2
data = {'代号': ['A', 'B', 'C', 'D'], '身高': [178, 177, 180, 175], '体重': [65, 70, 64, 67]}
df2 = pd.DataFrame(data)

# 以xlsxwriter为引擎，创建writer对象，并初始化文件名为pandas_simple.xlsx
writer = pd.ExcelWriter('pandas_moresheet.xlsx', engine='xlsxwriter')

# 将DataFrame存储到writer里面
df1.to_excel(writer, sheet_name='豆瓣图书')
df2.to_excel(writer, sheet_name='体测数据')

# 关闭writer对象，并保存写入的数据
writer.save()

# 读取xlsx文件
df = pd.read_excel('pandas_moresheet.xlsx', sheetname='体测数据')
print(df)
