'''
JD 秒杀
https://miaosha.jd.com/
'''


import re
import json
import requests
from fake_useragent import UserAgent


# 为了更好地输出显示json文件
def printjson(data):
    json_str = json.dumps(data, indent=4, ensure_ascii=False)
    print(json_str)

# 获取网页数据
def getdata(json_url):
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    data = requests.get(json_url, headers=headers)
    # print(data.text)

    # 正则表达式开启贪婪匹配模式，匹配到最外层的{}以包含所有内容
    re_data = re.findall('pcMiaoShaAreaList\(({.*})\)', data.text)[0]
    # 转化为json格式，方便处理
    json_data = json.loads(re_data)
    # printjson(json_data)

    # 观察到分为brandList和miaoshaList,我们以miaoshaList为例
    miaoShaList = json_data['miaoShaList']
    print(miaoShaList)
    print(len(miaoShaList))
    printjson(miaoShaList)



if __name__=='__main__':
    json_url1 = 'https://ai.jd.com/index_new?app=Seckill&action=pcMiaoShaAreaList&callback=pcMiaoShaAreaList&_=1493626377063'
    getdata(json_url1)








