import os
import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

# 　修改工作目录
if 'Myxlsxdata' not in os.listdir():
    os.mkdir('Myxlsxdata')
os.chdir('Myxlsxdata')

# 创建数据
data = {'代号': ['A', 'B', 'C', 'D'], '身高': [178, 177, 180, 175], '体重': [65, 70, 64, 67]}
df = pd.DataFrame(data)

# 创建工作簿
wb = Workbook()
# 　插入表
ws = wb.create_sheet("体测数据", 0)  # 0代表在开头插入，默认在末尾插入
# 插入数据
for r in dataframe_to_rows(df, index=True, header=True):
    ws.append(r)

wb.save("pandas_openpyxl.xlsx")

# 读取
df = pd.read_excel('pandas_openpyxl.xlsx')
print(df)
