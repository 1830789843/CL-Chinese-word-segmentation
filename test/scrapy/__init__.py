# 简单的网络爬虫
from urllib import request
# from urllib3 import request
import chardet

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
chaper_url = "https://www.jianshu.com/p/9bd5d9f8f6a5"
req = request.Request(url=chaper_url, headers=headers)
response = request.urlopen(req)
html = response.read()
charset = chardet.detect(html)   # {'language': '', 'encoding': 'utf-8', 'confidence': 0.99}
html = html.decode(str(charset["encoding"]))  # 解码

print(html)
