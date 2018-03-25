import re
import json
import time
import pickle
import requests
import urllib.request
from PIL import Image
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from yundama import getcode_from_yundama



# 提交表单登录并获取cookie

def get_cookie_from_net():

    url = 'https://accounts.douban.com/login'
    login_html = s.get(url, headers=headers).text

    try:
        verif_img_url = re.findall(r'<img id="captcha_image" src="(.*?)" alt="captcha"', login_html)[0]
        verif_img_data = s.get(verif_img_url, headers=headers).content

        with open('douban.jpg', 'wb') as f:
            f.write(verif_img_data)

    except:
        captha_id = captha_code = None
    else:
        # 获取captcha-id
        captha_id = re.findall(r'name="captcha-id" value="(.*?)"/>', login_html)[0]
        print('captcha_id: ', captha_id)

        # 云打码自动获取
        print("利用云打码获取识别验证码...")
        captha_code = getcode_from_yundama()
        if not captha_code:
            print('sleeping...')
            time.sleep(10)
            captha_code = getcode_from_yundama()

        # 手动输入验证码
        # img = Image.open('douban.jpg')
        # Image._show(img)
        # captha_img = str(input("输入验证码："))

    # 构建表单
    if captha_id==None:
        payload = {'source': 'None',
                   'redir': 'https://www.douban.com/',
                   'form_email': '你的邮箱',
                   'form_password': '你的密码',
                   'login': '登录'}

    else:
        payload = {'source': 'None',
                   'redir': 'https://www.douban.com/',
                   'form_email': '你的邮箱',
                   'form_password': '你的邮箱',
                   'captcha-solution': captha_code,
                   'captcha-id': str(captha_id),
                   'login': '登录'}
    print(payload)

    url = 'https://accounts.douban.com/login'
    data = s.post(url, headers=headers, data=payload, verify=True)  # 绕过了SSL验证
    with open('cookies.douban', 'wb') as f:
        cookiedict = requests.utils.dict_from_cookiejar(s.cookies)
        pickle.dump(cookiedict, f)
    print("提交表单登录，成功获取cookies...")
    '''
    这里可以用用户名进一步的验证是否登录成功
    '''
    if '不秩稚童' in data.text:
        print("登录成功！")

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
    data = getdata(html)
    print(data)


if __name__=='__main__':
    # 一些全局变量
    s = requests.session()
    ua = UserAgent()
    headers = {'User-Agent': ua.random}

    # 登录并获取数据
    login_and_getdata()


