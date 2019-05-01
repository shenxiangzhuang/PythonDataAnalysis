import requests
import pickle
from bs4 import BeautifulSoup


# 提交表单登录并获取cookie
def get_cookie_from_net():
    url = "https://accounts.douban.com/j/mobile/login/basic"
    # 构建表单
    payload = {
            "ck": "",
            "name": "your email",
            "password": "your password",
            "remember": "true",
            "ticket": ""
        }

    data = s.post(url, headers=headers, data=payload).json()
    # 检测登录是否成功
    if data["status"] == "success":
        print("登陆成功!")

    with open('cookies.douban', 'wb') as f:
        cookiedict = requests.utils.dict_from_cookiejar(s.cookies)
        pickle.dump(cookiedict, f)
    print("成功获取cookies!")

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

    html = s.get('https://www.douban.com/people/146448257/', headers=headers)
    # print(html.text)
    data = getdata(html)
    print(data)


if __name__ == '__main__':
    # 一些全局变量
    s = requests.session()
    # 这里务必更换
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6"}
    # 登录并获取数据
    login_and_getdata()
