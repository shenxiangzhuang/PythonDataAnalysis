import jieba
import pandas as pd
from snownlp import SnowNLP
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS
from scipy.misc import imread

# 读入处理好的数据
df = pd.read_csv('../data/douban_processed.csv')

# 预览数据
print(df.head(5))


# 分析评论文本

# 情感分析
def get_sentiments(origin_s):
    s = SnowNLP(origin_s)
    return s.sentiments


df['c_sentiments'] = df['c_data'].apply(get_sentiments)
df['c_sentiments'].plot.hist()
plt.savefig('../data/positive.png')
plt.show()

# 全部评论的关键字
all_comments = ''.join(df['c_data'])
all_snow = SnowNLP(all_comments)
keywords = all_snow.keywords(30)
print(keywords)

# 摘要
# ['故事里每个人的结局都很好', '大家都不是一个人', '每个人都有故事每个人都有视角每个人都有选择']
summary = all_snow.summary(3)
print(summary)

# 其他应用机器学习进行探索...

# 简单的可视化
sns.countplot('c_rank_num', data=df)
plt.savefig('../data/rank.png')
plt.show()


# 词云
def get_wordCloud(mylist):
    word_list = [" ".join(jieba.cut(sentence)) for sentence in mylist]
    new_text = ' '.join(word_list)
    pic_path = '../data/heart.png'
    img_mask = imread(pic_path)

    stopwords = set(STOPWORDS)
    stopwords.add("电影")
    wordcloud = WordCloud(background_color="white", max_words=2000, font_path='/home/shensir/Downloads/msyh.ttc',
                          mask=img_mask, stopwords=stopwords).generate(new_text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.savefig('../data/wordcloud.png')
    plt.show()


get_wordCloud(df['c_data'])
