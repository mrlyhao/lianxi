import requests
import re
import urllib.parse
import time

class Top(object):

    def __init__(self, banner):
        self.banner = banner
        self.titles = []
        self.links = []
        self.summary = {}
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"}

    def get_top(self, url):#获取热搜榜，并获取链接
        r = requests.get(url, headers=self.headers)
        html = r.text
        #微博热搜榜隐藏在源代码中，被解码为utf-8,并在其中随机插入‘25’干扰，正则提取，然后替换25，再编码为中文即可。
        pattern = re.compile(r'class=\\"star_name\\">.*?<a href=\\"\\\/weibo\\\/(.*?)&Refer=top')
        raw = re.findall(pattern,html)
        for i in raw:
            self.titles.append(i.replace('25', ''))
        for i in self.titles:
            names = urllib.parse.unquote(i)
            link = 'http://s.weibo.com/weibo/' + i
            self.links.append(link)
            time.sleep(1.5)
            print(names,"\n====================================================================")
            self.get_news(link)
            #print('Down One Hot')

    def get_news(self, link):
        titles = []
        contents = []
        r2 = requests.get(link, headers=self.headers)
        html2 = r2.text
        pattern = re.compile(r'feed_content wbcon.*?nick-name=\\"(.*?)\\" href=')#提取发布微博名称
        news = re.findall(pattern, html2)
        for new in news:
            b = new.encode()
            a = b.decode('unicode_escape')
            titles.append(a)
        pattern1 = re.compile(r'comment_txt.*?>(.*?)<\\\/p>')#提取发布的文字内容
        infos = re.findall(pattern1,html2)
        for info in infos:
            a= re.sub(r'\s|<.*?>|\\n|\\t', '',info)
            b = a.encode()
            c = b.decode('unicode_escape')
            contents.append(c)
        for title,content in zip(titles,contents):
            try:
                shuchu = '博主：{}\n内容：{}'.format(title,content)
                print(shuchu)
            except:
                continue

if __name__ == '__main__':

    realtimehot = Top('实时热搜榜')
    realtimehot.get_top("http://s.weibo.com/top/summary?cate=realtimehot")
