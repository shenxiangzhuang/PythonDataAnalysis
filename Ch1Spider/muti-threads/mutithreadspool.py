'''
多线程，多进程测试
参考：
http://stackoverflow.com/questions/2846653/how-to-use-threading-in-python
https://docs.python.org/3.6/library/multiprocessing.html#module-multiprocessing.dummy
http://cuiqingcai.com/3325.html
'''

import time
import requests
import concurrent
from concurrent import futures
import pandas as pd
import threading
from multiprocessing import Pool


# 装饰器，打印函数的执行时间
def gettime(func):
    def warapper(*args, **kwargs):
        print("=" * 50)
        print(func.__name__, 'Start...')
        starttime = time.time()
        func(*args)
        endtime = time.time()
        spendtime = endtime - starttime
        print(func.__name__, "End...")
        print("Spend", spendtime, "s totally")
        print("=" * 50)

    return warapper


# 从文件取n个网址测试
def get_urls_from_file(n):
    df = pd.read_csv('TestUrls.csv')  # 共1000个网址
    urls = list(df['url'][:n])

    return urls


# 请求并解析网页获取数据（这里简单把要获取的数据设为网页源码）
def getdata(url, retries=3):
    # print("正在下载:", url)
    headers = {}
    try:
        html = requests.get(url, headers=headers)
        # print(html)

    except requests.exceptions.ConnectionError as e:
        # print('下载出错[ConnectionError]:', e)
        html = None

        # 5xx 错误为服务器错误,我们可以进行重新请求
    if (html != None and 500 <= html.status_code < 600 and retries):
        retries -= 1
        # print('服务器错误正在重试...')
        getdata(url, retries)
        data = html.text
    else:
        data = None

    return data


# 串行
@gettime
def Mynormal():
    for url in urls:
        getdata(url)


# 进程池
@gettime
def MyprocessPool(num=10):
    pool = Pool(num)
    results = pool.map(getdata, urls)

    pool.close()
    pool.join()
    return results


# 多线程
@gettime
def Mymultithread(max_threads=10):
    # 对urls的处理
    def urls_process():
        while True:
            try:
                # 从urls末尾抽出一个url
                url = urls.pop()
            except IndexError:
                # urls爬取完毕，为空时，结束
                break
            data = getdata(url, retries=3)
            '''
            这里是对网页数据的提取与存储操作
            '''

    threads = []

    # 未达到最大线程限制且仍然存在带爬取的url时，可以创建新的线程进行加速
    while int(len(threads) < max_threads) and len(urls):
        thread = threading.Thread(target=urls_process)
        # print('创建线程', thread.getName())
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


# 线程池
@gettime
def Myfutures(num_of_max_works=10):
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_of_max_works) as executor:
        executor.map(getdata, urls)


if __name__ == '__main__':
    # 　取100个网页做测试
    urls = get_urls_from_file(100)
    Mynormal()  # 串行
    MyprocessPool(10)  # 进程池
    Myfutures(10)  # 线程池
    Mymultithread(10)  # 多线程

'''

100个网页

==================================================
Mynormal Start...
Mynormal End...
Spend 20.605727672576904 s totally
==================================================
==================================================
MyprocessPool Start...
MyprocessPool End...
Spend 2.4525890350341797 s totally
==================================================
==================================================
Mymutithread Start...
Mymutithread End...
Spend 2.1947641372680664 s totally
==================================================
==================================================
Myfutures Start...
Myfutures End...
Spend 2.1515889167785645 s totally
==================================================

'''
