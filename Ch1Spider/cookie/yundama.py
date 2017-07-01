'''
参考：
http://www.bigdataway.net/index.php/node/4324
http://www.yundama.com/download/YDMHttp.html
'''
import json
import time
import requests

def getcode_from_yundama():

    captcha_username = '你的用户名'
    captcha_password = '你的密码'
    captcha_id = 1
    captcha_appkey = '你的KEY'
    captcha_codetype = '3000'
    captcha_url = 'http://api.yundama.com/api.php?method=upload'
    captcha_result_url = 'http://api.yundama.com/api.php?cid{}&method=result'
    filename = 'douban.jpg'
    timeout = 30

    postdata = {'method': 'upload', 'username': captcha_username,
                'password': captcha_password, 'appid': captcha_id,
                'appkey': captcha_appkey, 'codetype': captcha_codetype,
                'timeout': timeout}

    fo = open(filename, 'rb')
    file = {'file': fo.read()}
    response = requests.post(captcha_url, postdata, files=file).text
    print(response)
    fo.close()

    response = json.loads(response)
    code = response['text']
    status = response['ret']
    if status == 0:
        print("识别成功！")
        print('验证码为：', code)

    return code
