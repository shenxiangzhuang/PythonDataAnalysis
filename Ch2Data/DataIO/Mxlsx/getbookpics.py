import os
import requests
import pandas as pd


# 获取所有图书的封面图片,以书名为文件名
def savepics(img_urls, titles):
    for i in range(len(img_urls)):
        img_url = img_urls[i]
        title = titles[i]
        img_data = requests.get(img_url).content  # 二进制内容
        # 存储图片
        with open(str(title) + '.jpg', 'wb') as f:
            f.write(img_data)


if __name__ == '__main__':
    # 为了数据文件和程序文件的分离,我们可以选择新建文件夹,并在此文件夹下进行文件的读写
    if 'Myxlsxdata' not in os.listdir():
        os.mkdir('Myxlsxdata')
    os.chdir('Myxlsxdata')

    books_data = pd.read_csv('result.csv')  # 读入爬取的数据
    img_urls = books_data['img_urls']  # 图片地址
    titles = books_data['titles']  # 图书名,为图片命名
    savepics(img_urls, titles)
