# coding:utf-8

import re
from urllib import request
import ssl
import string

def getHtml(url):  # 爬取网页html
    page = request.urlopen(url)
    html = page.read()
    return html

ssl._create_default_https_context = ssl._create_unverified_context
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
chaper_url = "https://www.people.com.cn/"
req = request.Request(url=chaper_url, headers=headers)

html = getHtml(req)
html = html.decode('gbk', "ignore")
# print(html)


def getFile(html):  # 获取网页链接的方法
    # 利用正则表达式匹配网页里的网页地址
    reg = r'href="([.*\S]*\.html)"'
    filere = re.compile(reg)
    filelist = re.findall(filere, html)
    print(filelist)
    return filelist


fileList = getFile(html)
fileCount = 0
# for把获取到的图片都下载到本地pic文件夹里，保存之前先在本地建一个pic文件夹
for filePath in fileList:
    f = open("../html/"+str(fileCount)+".txt", 'wb')
    content = getHtml(filePath).decode("gbk")
    # print(content)
    reg = r'class="fl text_con_left"'
    filere = re.compile(reg)
    result = re.findall(filere, content)

    print(result)
    # break
    # f.write((request.urlopen(filePath)).read())
    f.close()
    fileCount += 1


print(fileCount)
print("全部抓取完成")
# print fileCount
# print "全部抓取完成"
