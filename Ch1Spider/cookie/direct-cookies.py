import requests
from fake_useragent import UserAgent

mycookie_fromcopy = ''  # 这里填上从浏览器复制而来的cookie信息

ua = UserAgent()
headers = {'User-Agent': ua.random,
           'Cookie': mycookie_fromcopy}
url = "https://www.douban.com/people/146448257/"  # 这里是登录之前访问不到的个人信息页面
data = requests.get(url, headers=headers)

print(data.status_code)
print(data.request.headers)
print(data.text)
