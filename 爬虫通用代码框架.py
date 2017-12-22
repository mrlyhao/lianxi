#-*- coding: UTF-8 -*-
import requests

def gethtmltext(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return  '产生异常'

if __name__ =="__main__":
    url = 'www.baidu.com'
    print(gethtmltext(url))