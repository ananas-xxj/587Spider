import urllib.request
from lxml import etree
from os import system
import re
#网站：http://www.587kan.com/ 爬取唯美素材主题的内容
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    , "referer": "http://www.587kan.com/weimeisucai/"}

#循环每一个分页的地址
def kantuhome():
    request = urllib.request.Request("http://www.587kan.com/weimeisucai/", headers=header)
    html = urllib.request.urlopen(request)
    readData = html.read()
    etree_html = etree.HTML(readData)
    xpaths = etree_html.xpath('//div[@id="pageNum"]/li/a/@href')
    for i in range(len(xpaths)):
        getNumPage("http://www.587kan.com/weimeisucai/" + xpaths[i])

#拿到一个分页里面每一个头像的地址
def getNumPage(pageUrl):
    print("pageurl:" + pageUrl)
    request = urllib.request.Request(pageUrl, headers=header)
    html = urllib.request.urlopen(request)
    readData = html.read()
    etree_html = etree.HTML(readData)
    xpaths = etree_html.xpath('//div[@class="touxiang_list"]/ul/li/a/@href')
    for i in range(len(xpaths)):
        getItemPage("http://www.587kan.com" + xpaths[i])

#每一个人物写真的分页
def getItemPage(ablumUrl):
    print("ablumUrl:" + ablumUrl)
    request = urllib.request.Request(ablumUrl, headers=header)
    html = urllib.request.urlopen(request)
    readData = html.read()
    etree_html = etree.HTML(readData)
    xpaths = etree_html.xpath('//div[@class="pages"]/ul/li/a/@href')
    sub = re.sub(r'/\d.*', "", ablumUrl)
    for i in range(len(xpaths)):
        getAblumItemPage(sub + "/" + xpaths[i])

#最后的单张图片保存下载到本地
def getAblumItemPage(ablumItemUrl):
    try:
        request = urllib.request.Request(ablumItemUrl, headers=header)
        html = urllib.request.urlopen(request)
        readData = html.read()
        etree_html = etree.HTML(readData)
        urls = etree_html.xpath('//div[@class="picbox"]/ul/li/imgkk/a/img/@src')
        names = etree_html.xpath('//div[@class="picbox"]/ul/li/imgkk/a/img/@alt')
    except:
        pass
    for i in range(len(urls)):
        imgUrl = "http:" + urls[i]
        print("urls:" + imgUrl)
        replace = str(names[i]).replace(" ", "")
        print("names:" + replace)
        try:
            request = urllib.request.Request(imgUrl, headers=header)
            html = urllib.request.urlopen(request)
            readData = html.read()
            imgFile = open('%s.jpg' % (replace), "wb")
            imgFile.write(readData)
            imgFile.close()
        except:
            pass


kantuhome()  # 开始爬虫
system('shutdown -s')
