import re
import requests
import pandas as pd
from fake_useragent import UserAgent

url = 'https://www.hao123.com/'
ua = UserAgent()
headers = {'User-Agent': ua.random}

resp = requests.get(url, headers)
data = resp.text
urls = re.findall(r'href="(http.*?)"', data)

df = pd.DataFrame()

# 我们取前1000个
df['url'] = urls[:1000]
df.to_csv('TestUrls.csv', index=None)
