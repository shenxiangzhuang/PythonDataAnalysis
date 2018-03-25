'''

xlsxwriter基本用法
http://www.python-excel.org/

'''

import os

import pandas as pd
import xlsxwriter

# 为了数据文件和程序文件的分离,我们可以选择新建文件夹,并在此文件夹下进行文件的读写
if 'Myxlsxdata' not in os.listdir():
    os.mkdir('Myxlsxdata')

# 切换到此文件夹下
os.chdir('Myxlsxdata')

# 导入数据,只导入需要的列.若有缺失值,显示为NULL
books_data = pd.read_csv('result.csv', usecols=['titles', 'authors', 'ratings', 'details'], na_values='NULL')
titles = books_data['titles']
authors = books_data['authors']
ratings = books_data['ratings']
details = books_data['details']

# 新建文件名为Books.xlsx的电子表格工作薄
workbook = xlsxwriter.Workbook('Books.xlsx')

# 为创建的电子表格增加一个名为表1的表格,默认表名为sheet1, sheet2...
worksheet = workbook.add_worksheet('豆瓣新书')

# 写入数据
nums = len(titles)  # 数据量

# 第一行写入列名
worksheet.write(0, 0, '图书封面')
worksheet.write(0, 1, '图书标题')
worksheet.write(0, 2, '图书作者')
worksheet.write(0, 3, '图书评价')
worksheet.write(0, 4, '图书细节')

# 根据内容设置列宽
worksheet.set_column('A:A', 20)
worksheet.set_column('B:B', 20)
worksheet.set_column('C:C', 20)
worksheet.set_column('D:D', 10)
worksheet.set_column('E:E', 150)

# 插入图片和文本数据
for i in range(1, nums):
    worksheet.insert_image(i, 0, titles[i] + '.jpg')
    worksheet.write(i, 1, titles[i])
    worksheet.write(i, 2, authors[i])
    worksheet.write(i, 3, ratings[i])
    worksheet.write(i, 4, details[i])

# 存储数据,关闭工作簿
workbook.close()
