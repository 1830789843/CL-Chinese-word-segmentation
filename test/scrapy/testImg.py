import re
from urllib import request


def getHtml(url):  # 爬取网页html
    page = request.urlopen(url)
    html = page.read()
    return html


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
chaper_url = "http://tieba.baidu.com/p/3205263090"
req = request.Request(url=chaper_url, headers=headers)

html = getHtml(req)
html = html.decode('UTF-8')
# print(html)


def getImg(html):  # 获取图片链接的方法
    # 利用正则表达式匹配网页里的图片地址
    reg = r'src="([.*\S]*\.jpg)" pic_ext="jpeg"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    return imglist


imgList = getImg(html)
imgCount = 0
# for把获取到的图片都下载到本地pic文件夹里，保存之前先在本地建一个pic文件夹
for imgPath in imgList:
    f = open("../pic/"+str(imgCount)+".jpg", 'wb')
    f.write((request.urlopen(imgPath)).read())
    f.close()
    imgCount += 1

print("全部抓取完成")
