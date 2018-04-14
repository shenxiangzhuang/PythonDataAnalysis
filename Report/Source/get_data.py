'''
豆瓣影评爬取：《奇迹男孩》
登录后爬取，也只爬取了点赞数最高的500条评价，（服务器端限制了用户可以查看的条数）
'''

import re
import time
import csv
from bs4 import BeautifulSoup


# 获取所有数据
def get_all_data(login_session, headers):
    # 创建文件，用来存储数据
    file = open('../data/douban.csv', 'w')
    csv_file = csv.writer(file)
    # 开始爬取
    page_urls = get_page_urls()
    for page_url in page_urls:
        try:
            time.sleep(0.05)
            page_data = login_session.get(page_url, headers=headers)
            page_obj = BeautifulSoup(page_data.text, 'lxml')
            comment_blocks = get_page_data(page_obj)
            for comment_block in comment_blocks:
                get_one_com_data(comment_block, csv_file)
        except Exception as e:
            print(page_url)
            print(e)
    file.close()


# 获取所有短评的URL（找规律）
def get_page_urls():
    page_urls = ["https://movie.douban.com/subject/26787574/comments?" \
                 "start=%s&limit=20&sort=new_score&status=P&percent_type=" % (start)
                 for start in range(0, 500, 20)]
    return page_urls


# 获取每页的短评信息
def get_page_data(page_obj):
    comment_blocks = page_obj.find('div', {'id': 'comments'}) \
        .find_all('div', {'class': 'comment-item'})
    return comment_blocks


# 获取单个短评的信息
def get_one_com_data(comment_block, csv_file):
    try:
        # 评价人数据
        p_data = comment_block.find('a', {'class': ''})
        # 评价人ID
        p_name = p_data.get('title')
        # 评价人主页
        p_url = p_data.get('href')
        # 评价具体数据
        # 评价日期
        c_date_time = comment_block.find('span', {'class': 'comment-time '}).get('title')
        # 评价内容
        c_data = comment_block.find('p', {'class': ''}).get_text()
        # 评级 [在bs4中同样可以使用re，可以解决很多问题]
        # 有些人未评等级
        try:
            c_rank = comment_block.find('span', class_=re.compile('allstar\d+ rating')).get('title')
        except:
            c_rank = None
            pass
        # 推荐（点赞）人数
        c_recom = comment_block.find('span', {'class': 'votes'}).get_text()
        # 将数据写入文件
        if c_rank != None:
            csv_file.writerow([p_name, p_url, c_date_time, c_data, c_rank, c_recom])
        return [p_name, p_url, c_date_time, c_data, c_rank, c_recom]
    except Exception as e:
        print(e)
        # print(comment_block)
