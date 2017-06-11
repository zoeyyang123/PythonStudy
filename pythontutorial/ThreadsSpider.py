# -*- coding: utf-8 -*-
"""
Created by zhaoyi on 17-6-11.
"""
import os
import urllib.request
import threading
import re

reg = r'img src=\'(.+?\.(jpg|gif))\''#正则表达式 要搞清楚懒惰模式
imgre = re.compile(reg)

class downloader(threading.Thread):
    def __init__(self, url, name):
        threading.Thread.__init__(self)
        self.url=url
        self.name=name
    def run(self):
        print ('downloading from %s' % self.url)
        opener=urllib.request.build_opener() #要用这种方式打开url 并伪装浏览器header
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(self.url,'/home/zhaoyi/图片/temp/'+self.name)#下载并保存到固定位置并命名


threads = [] #多线程 要用= []初始化

def main(url):
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1')]
    html = opener.open(url).read()
    text= html.decode('utf-8', 'ignore')#要将html转码从byte到string 并忽略掉不能识别的字符
    groups=re.findall(reg, text)
    x = 0
    for g in groups:
        nameUrl=g[0].split('/')#将图片网址分割
        name = nameUrl[g[0].count('/')]#查询分割次数，并取值
        path=g[0]

        t=downloader(path, name)
        threads.append(t)
        t.start()

if __name__ == '__main__':
    main("http://cl.friu.pw/htm_data/7/1705/2419539.html")
    for t in threads:
        t.join()