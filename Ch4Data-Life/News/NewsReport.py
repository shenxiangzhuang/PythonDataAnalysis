import requests
import os
import time
import chardet
from bs4 import BeautifulSoup
from MEmail import send_ms

# 获取网页数据
def get_web_data(url):
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36"}
    html = requests.get(url, headers=headers)
    Encoding = chardet.detect(html.content)['encoding']
    html.encoding = Encoding
    web_data = html.text

    return web_data

# 获取标题及对应链接
def get_titles(web_data):
    title_hrefs = {}
    soup = BeautifulSoup(web_data, 'lxml')
    titles_data = soup.find_all({'a': {'target': '_blank'}})

    for title in titles_data:
        title_text = title.get_text()

        # 过滤一些无关的标签等[长度一般较短]
        if len(title_text) >= 10:
            if title.has_attr('href'):
                href = title['href']
            else:
                href = 'Cannot find link...'

            title_hrefs[title_text] = href

    return title_hrefs


# 筛选自己想了解的信息
def get_roi(title_hrefs, key_words):
    roi = {}  # 用于存储感兴趣的标题
    for title in title_hrefs:
        if key_words in title:
            roi[title] = title_hrefs[title]

    return roi

# 生成本地日志记录
def record(roi, key_words):
    if 'NewsReportLog.txt' not in os.listdir():
        with open('NewsReportLog.txt', 'w') as f:  # 写入模式
            f.write(str(key_words)+'相关新闻抓取程序日志'+str(time.ctime())+'\n')

    with open('NewsReportLog.txt', 'a') as f:  # 追加模式
        f.write('='*10+str(time.ctime()+'='*10))
        for title in roi:
            f.write(title)
            f.write(roi[title])

        f.write('\n')

# 发送邮件到邮箱提醒
def send_report(roi):
    length = len(roi)
    s1 = '本次共探测到'+str(length)+'条相关新闻'+'\n'
    s2 = ''
    for title in roi:
        s2 += title
        s2 += roi[title]
        s2 += '\n'
    send_ms(s1+s2)


if __name__=='__main__':
    web_data = get_web_data("http://tech.baidu.com/")
    titles = get_titles(web_data)
    key_words = 'iPhone'
    roi = get_roi(titles, key_words)
    print(roi)
    if len(roi) != 0:
        record(roi, key_words)
        send_report(roi)

