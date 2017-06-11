# -*- coding: utf-8 -*-
"""
Created by zhaoyi on 17-6-10.
"""
import urllib
import urllib.request
import re



def Read(url):
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1')]
    html = opener.open(url).read()
    return html.decode('utf-8', 'ignore')

def getImg(html):
    reg = r'img src=\'(.+?\.(jpg|gif))\''
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    opener=urllib.request.build_opener()
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1')]
    urllib.request.install_opener(opener)
    x = 0
    for imgurl in imglist:
        tmp = str(imgurl[0])
        ttmp = tmp.split('/')
        s = tmp.count('/')
        urllib.request.urlretrieve(tmp, '%s.gif' % x, cbk)
        x+=1

def cbk(a,b,c):
    '''''回调函数 
    @a:已经下载的数据块 
    @b:数据块的大小 
    @c:远程文件的大小 
    '''
    per=100.0*a*b/c
    if per>100:
        per=100
    print('%.2f%%' % per)

html = Read("hhttp://cl.friu.pw/htm_data/7/1705/2414794.html")

getImg(html)