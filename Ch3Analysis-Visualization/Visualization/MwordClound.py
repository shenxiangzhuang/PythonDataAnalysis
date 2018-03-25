import jieba
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from scipy.misc import imread


def get_wordList():
    df = pd.read_excel('完美陌生人-短评.xlsx')
    wordList = df['评论内容'].tolist()
    return wordList


def get_wordClound(mylist):
    word_list = [" ".join(jieba.cut(sentence)) for sentence in mylist]
    new_text = ' '.join(word_list)
    pic_path = 'mask.jpg'
    img_mask = imread(pic_path)

    wordcloud = WordCloud(background_color="white", font_path='/home/shen/Downloads/font/msyh.ttc',
                          mask=img_mask, stopwords=STOPWORDS, ).generate(new_text)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


if __name__ == '__main__':
    wordList = get_wordList()
    get_wordClound(wordList)
