import re
import pandas as pd

# 读入数据，给定各字段的名字
df = pd.read_csv('../data/douban.csv', header=None, skip_blank_lines=True,
                 names=['p_name', 'p_url', 'c_date_time', 'c_data', 'c_rank', 'c_recom'])

# 预览数据
# print(df.head(5))

# 缺失值检测与去除
print(df.isnull().sum())
df.dropna(inplace=True)


# 拆分原c_date_time为c_date和c_time
def get_date(date_time):
    # 有时会格式不对
    if len(date_time) < 10:
        return None
    return re.findall(r'(\d+-\d+-\d+) \d+.*?', date_time)[0]


def get_time(date_time):
    if len(date_time) < 10:
        return None
    return re.findall(r'.*? (\d+:\d+:\d+)', date_time)[0]


df['c_date'] = df['c_date_time'].apply(get_date)
df['c_time'] = df['c_date_time'].apply(get_time)

# 如果需要，也可以进行数据类型的转换
print(df.dtypes)
df['c_date_time'] = df['c_date_time'].astype('datetime64[ns]')
print(df.dtypes)


# 也可方便地进行数据转换[Encoding Categorical Values]
# 将汉字对应编码为数字
def trans(words):
    if words == '力荐':
        return 5
    elif words == '推荐':
        return 4
    elif words == '还行':
        return 3
    elif words == '较差':
        return 2
    elif words == '很差':
        return 1
    else:
        return None


df['c_rank_num'] = df['c_rank'].apply(trans)

# 设置索引列为c_date_time
df.index = df['c_date_time']

# 去除多余的c_date_time列
df = df.drop(['c_date_time'], axis=1)

# 其他的一些操作...

# 去除操作产生的缺失值
df.dropna(inplace=True)
# 保存预处理后的文件
df.to_csv('../data/douban_processed.csv')
