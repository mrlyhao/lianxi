# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import thread
import time

class QSBK:

    def __int__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        self.headers = {'User-Agent':self.user_agent}
        self.stories = []
        self.enable = False

    def getpage(self,pageIndex):
        try:
            url = 'https://www.qiushibaike.com/8hr/page/'+str(pageIndex)
            request = urllib2.Request(url,headers=self.headers)
            response = urllib2.urlopen(request)
            pageCode = response.read().decode('utf-8')
            return pageCode
'''
        except urllib2.URLError,e:
            if hasattr(e,'reason'):
                print(u'连接糗事百科失败，错误原因',e.reason)
                return None

    def getpageItems(self,pageIndex):
        pageCode = self.getpage(pageIndex)
        if not pageCode:
            print'页面加载失败'
            return None
        pattern = re.compile('<h2>(.*?)</h2>.*?<div class="content">.*?<span>(.*?)</span>',re.S)
        items = re.findall(pattern,pageCode)
        data = []
        for item in items:
            haveImg = re.search('img',item[1])
            if not haveImg:
                 data.append([item[0].strip(),item[1].strip()])
        return data

    def loadpage(self):
        if self.enable == True:


            if len(self.stories)< 2 :
                data =self.getpage(self.pageIndex)
                if data:
                    self.stories.append(data)
                    self.pageIndex += 1

    def getOneStory(self,data,nowPage):
        for story in data:
            input = raw_input()
            self.loadpage()
            if input == 0:
                self.enable = False
                return nowPage
            print(u'第%d页发布人:%s发布内容:%s'%(nowPage,story[0],story[1]))

    def start(self):
        print(u'正在读取糗事百科，按回车查看新段子')
        self.enable = True
        self.loadpage()
        nowPage = 0
        while self.enable:
            if len(self.stories)>0:
                pageStories = self.stories[0]
                nowPage+=1
                del self.stories[0]
                self.getOneStory(pageStories,nowPage)

spider = QSBK()
spider.start()
'''