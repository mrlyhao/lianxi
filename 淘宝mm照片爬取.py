import re
import requests
from bs4 import BeautifulSoup
import time

def getHTMLtext(URL):
    try:
        r = requests.get(URL,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('cuowu')

def getContents(html_text):
    try:
        pattern = re.compile('<div class="list-item">.*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name".*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>',re.S)
        items = re.findall(pattern,html_text)
        contents= []
        for item in items:
            contents.append([item[0],item[1],item[2],item[3],item[4]])
        return contents
    except:
        return ''

def getMMinfotext(infoURL):
    try:
        r = requests.get(infoURL,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('cuowu')

def getBrief(info):
    try:
        soup = BeautifulSoup(info,'htnl.parser')

    except:
        return ''


def main():
    Url = 'https://mm.taobao.com/json/request_top_list.htm?page=1'
    Html_text = getHTMLtext(Url)
    getContents(Html_text)


main()