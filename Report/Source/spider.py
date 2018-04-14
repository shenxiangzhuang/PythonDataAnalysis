import requests
import pickle
from bs4 import BeautifulSoup
from get_data import get_all_data


# 提交表单登录并获取cookie
def get_cookie_from_net():
    url = 'https://accounts.douban.com/login'
    # 构建表单
    payload = {'source': 'None',
               'redir': 'https://www.douban.com/',
               'form_email': '你的邮箱',
               'form_password': '你的密码',
               'login': '登录'}

    data = s.post(url, headers=headers, data=payload, verify=True)  # 绕过了SSL验证
    with open('cookies.douban', 'wb') as f:
        cookiedict = requests.utils.dict_from_cookiejar(s.cookies)
        pickle.dump(cookiedict, f)
    print("提交表单登录，成功获取cookies...")

    return s.cookies


# 从cookie文件获取cookie
def get_cookie_from_file():
    with open('cookies.douban', 'rb') as f:
        cookiedict = pickle.load(f)
        cookies = requests.utils.cookiejar_from_dict(cookiedict)
    print("解析文件，成功提取cookis...")
    return cookies


# 假设这里我要获取自己的签名数据
def getdata(html):
    soup = BeautifulSoup(html.text, 'lxml')
    mydata = soup.select('#display')[0].get_text()
    '''
    这里进行登录后其他数据的获取及存储，这里仅仅获取了自己的签名数据。
    '''
    return mydata


def login_and_getdata():
    print('获取cookis...')
    try:
        s.cookies = get_cookie_from_file()
    except:
        print("从文件获取cookies失败...\n正在尝试提交表单登录以获取...")
        s.cookies = get_cookie_from_net()
    # 开始爬取数据
    get_all_data(s, headers)


if __name__ == '__main__':
    # 一些全局变量
    s = requests.session()
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWe'
                             'bKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

    # 登录并获取数据
    login_and_getdata()
