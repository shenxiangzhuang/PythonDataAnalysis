import re
import time
import chardet
import requests
import urllib.robotparser
from fake_useragent import UserAgent


# 获取headers
def get_headers():
    ua = UserAgent()
    user_agent = ua.random
    headers = {'User-Agent': user_agent}

    return headers


# 这里获取代理IP的函数直接给出了proxies,
# 我们也可以用此函数去爬取免费的代理IP，因为不是重点，这里不再赘述
def get_proxies():
    proxies = {
        "http": "125.88.74.122:84",
        "http": "123.84.13.240:8118",
        "https": "94.240.33.242:3128"
    }

    return proxies


# robots.txt检测
def robot_check(robotstxt_url, headers, url):
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(robotstxt_url)
    rp.read()
    result = rp.can_fetch(headers['User-Agent'], url)

    return result


# 获取网页数据, 这里我们没有返回data.text,
# 因为抓取图片图片时返回的应该是data.content
def get_data(url, num_retries=3, proxies=None):
    try:
        data = requests.get(url, timeout=5, headers=headers)
        print(data.status_code)
    except requests.exceptions.ConnectionError as e:
        print("请求错误, url:", url)
        print("错误详情:", e)
        data = None
    except:  # other error
        print("未知错误, url:", url)
        data = None

    if (data != None) and (500 <= data.status_code < 600):
        if (num_retries > 0):
            print("服务器错误，正在重试...")
            time.sleep(1)
            num_retries -= 1
            get_data(url, num_retries, proxies=proxies)

    return data


# 对网页内容的解析，提取和存储等操作
def parse_data(data):
    if data == None:
        return None

    charset = chardet.detect(data.content)
    data.encoding = charset['encoding']
    html_text = data.text
    '''
    对网页数据的解析提取等操作,假设这里要获取网页的title
    '''
    interesting_data = re.findall('<title>(.*?)</title>', html_text)

    return interesting_data


if __name__ == '__main__':
    headers = get_headers()
    proxies = get_proxies()
    data = get_data("http://www.baidu.com", num_retries=3, proxies=proxies)
    interesting_data = parse_data(data)
    print(interesting_data)
