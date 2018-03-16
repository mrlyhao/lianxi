## 使用账号密码加密登录微博
微博的账号和密码都是经过加密的，账号是用base64加密，密码是使用rsa加密的。然后先访问微博一次获取servertime，nonce，pubkey，raskv。然后与passwd加密成为加密后的密码sp。然后设置post参数后登录。
```
# 导入所需模块
import urllib.error
import urllib.request
import urllib.parse
import requests
import re
import rsa
import http.cookiejar  #从前的cookielib
import base64
import json
import urllib
import binascii

def login(username,password):
    #打开一个session后续操作继承cookie
    session = requests.Session()
    #微博的username使用base64加密，显然username变成url编码，然后加密
    username = urllib.request.quote(username)
    su = base64.b64encode(username.encode(encoding='utf-8')).decode('utf-8')
    #代开一个带有username的链接获取post的部分随机参数。
    url_prelogin = 'http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=&' +  su + '&rsakt=mod&client=ssologin.js(v1.4.19)'
    resp = session.get(url_prelogin)
    #正则提取这些参数
    json_data = re.findall(r'\((.*?)\)',resp.text)[0]
    data = json.loads(json_data)

    servertime = data['servertime']
    nonce = data['nonce']
    pubkey = data['pubkey']
    raskv = data['rsakv']
    #微博的密码是rsa加密的，获取加密后的password
    rsa_e = int('10001', 16)  # 0x10001
    pw_string = str(servertime) + '\t' + str(nonce) + '\n' + str(password)
    key = rsa.PublicKey(int(pubkey, 16), rsa_e)
    pw_encypted = rsa.encrypt(pw_string.encode('utf-8'), key)
    sp = binascii.b2a_hex(pw_encypted).decode('utf-8')
    post_data = {
        "entry": "weibo",
        "gateway": "1",
        "from": "",
        "savestate": "7",
        "qrcode_flag": 'false',
        "useticket": "1",
        "pagerefer": "https://login.sina.com.cn/crossdomain2.php?action=logout&r=https%3A%2F%2Fweibo.com%2Flogout.php%3Fbackurl%3D%252F",
        "vsnf": "1",
        "su": su,
        "service": "miniblog",
        "servertime": servertime,
        "nonce": nonce,
        "pwencode": "rsa2",
        "rsakv": raskv,
        "sp": sp,
        "sr": "1680*1050",
        "encoding": "UTF-8",
        "prelt": "194",
        "url": "https://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack",
        "returntype": "META"
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",

    }
```
但是登录后获得的并不是只记得代码，还需要经过三次的跳转才能正式获取到信息
```
    #正式登录微博要经历三次跳转。
    url_login = 'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.19)'
    try:
        resp = session.post(url_login,data=post_data,headers=headers)
        #提取response中location.replace的链接然后打开此链接
        login_url = re.findall('location\.replace\("(.*?)"\)',resp.content.decode('GBK'))[0]
        respo = session.get(login_url)
        # 继续提取response中location.replace的链接然后打开此链接
        login_url_1 = re.findall("location\.replace\('(.*?)'\)", respo.content.decode('GBK'))[0]
        # 提取response中的userdomain，然后访问得到正式的内中。注意此处要加headers
        resp_1 = session.get(login_url_1,headers=headers).content.decode('GBK')
        login_url_2 = 'http://weibo.com/'+ re.findall(r'"userdomain":"(.*?)"',resp_1)[0]
        final=session.get(login_url_2,headers=headers).text
        print(final)
        return final
    except BaseException as e:
        print(e)
login(username='liyuanhaode@sina.cn',password='******')
```
## 使用selenium登录微博
### 先 使用selenium打开Chrome然后输入账号密码登录，然后获取cookies。经过处理后变成可传入headers的cookies。
```
from selenium import webdriver
from scrapy.selector import Selector
import time
import requests
import re
#使用selenium登录并获取cookie，然后使用cookies登录
def get_cookies():
    #打开chrome浏览器
    browser = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
    #浏览器最大化
    browser.maximize_window()
    #打开登录页面
    browser.get('https://weibo.com/login.php')
    #等待3秒，确保加载完成
    time.sleep(3)
    #填写账号
    browser.find_element_by_css_selector('#loginname').send_keys('liyuanhaode@sina.cn')
    #填写密码
    browser.find_element_by_css_selector('.info_list.password input[node-type="password"]').send_keys('******')
    #点击登录
    browser.find_element_by_css_selector('.info_list.login_btn a[node-type="submitBtn"]').click()
    #获取cookies
    a= browser.get_cookies()
    #把cookie有dict变成str
    cookie = [item["name"] + "=" + item["value"] for item in a]
    cookiestr = ';'.join(item for item in cookie)
    return  cookiestr
```
### 然后使用requsets.Session登录。获取微博页面信息。
```
def login():
    #打开一个session后续操作继承cookie
    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
        "Cookie":get_cookies()
    }
    url = 'https://weibo.com/tianliang1979?is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&page=1#feedtop'
    info_1=session.get(url,headers=headers)
    print(info_1.content.decode('utf-8'))
```
# python文件合集


* 使用scrapy 批量采集MM图片 [点击查看](https://github.com/mrlyhao/mmscrapy)
* 使用scrapy爬取拉勾网职位信息，并异步保存在mysql中[点击查看](https://github.com/mrlyhao/bole/tree/master/bole)
* 使用scrapy-redis爬取拉勾，Windows为slave，linux为master。[点击下载](https://github.com/mrlyhao/lagou_redis)
* [爬取小说站](https://github.com/mrlyhao/lianxi/tree/master/test1)

* 使用两种方法模拟登录微博 [点击查看](https://github.com/mrlyhao/lianxi/blob/master/%E5%BE%AE%E5%8D%9A%E6%A8%A1%E6%8B%9F%E7%99%BB%E5%BD%95.py)
* 模拟登录后爬取移动端微博大V数据[点击查看](https://github.com/mrlyhao/lianxi/blob/master/%E7%88%AC%E5%8F%96%E5%BE%AE%E5%8D%9A%E4%B8%AA%E4%BA%BA%E9%A1%B5%E9%9D%A2.py)
* 使用beautifulsoup 批量抓取MM照片 [点击查看](https://github.com/mrlyhao/lianxi/blob/master/mm%E7%85%A7%E7%89%87%E6%89%B9%E9%87%8F%E7%88%AC%E5%8F%96.py)
* 采集后台数据，分析每本书的情况 [点击查看](https://github.com/mrlyhao/lianxi/blob/master/%E4%B9%A6%E4%B8%9B%E5%90%8E%E5%8F%B0%E6%95%B0%E6%8D%AE%E9%87%87%E9%9B%86.py)
* 采集京东数据并保存在表格中 [点击查看](https://github.com/mrlyhao/lianxi/blob/master/%E4%BA%AC%E4%B8%9C%E7%88%AC%E8%99%AB.py)和[pandas版本](https://github.com/mrlyhao/lianxi/blob/master/%E4%BA%AC%E4%B8%9C%E7%88%AC%E8%99%ABpandas.py)
* 简单爬取淘宝数据 [点击查看](https://github.com/mrlyhao/lianxi/blob/master/%E6%B7%98%E5%AE%9D%E5%95%86%E5%93%81%E4%BF%A1%E6%81%AF%E5%AE%9A%E5%90%91%E7%88%AC%E8%99%AB.py)
* 爬取网上ip验证后储存 [点击查看](https://github.com/mrlyhao/lianxi/blob/master/%E5%A4%9AIP%E4%BB%A3%E7%90%86.py)
* 爬取妹子图，解决图片重定向问题 [点击查看](https://github.com/mrlyhao/lianxi/blob/master/%E5%A6%B9%E5%AD%90%E5%9B%BE.py)
* 有道翻译输入查询词，并爬取结果 [点击查看](https://github.com/mrlyhao/lianxi/blob/master/%E6%9C%89%E9%81%93%E7%BF%BB%E8%AF%91%E6%8F%90%E4%BA%A4.py)
* 简单爬取今日头条 [点击查看](https://github.com/mrlyhao/lianxi/blob/master/%E7%88%AC%E5%8F%96%E4%BB%8A%E6%97%A5%E5%A4%B4%E6%9D%A1.py)`和今日头条美女图` [点击查看](https://github.com/mrlyhao/lianxi/blob/master/%E7%88%AC%E5%8F%96%E4%BB%8A%E6%97%A5%E5%A4%B4%E6%9D%A1%E7%BE%8E%E5%A5%B3%E5%9B%BE.py)
* 使用selenium爬取空间说说 [点击查看](https://github.com/mrlyhao/lianxi/blob/master/%E7%88%AC%E5%8F%96%E5%A5%BD%E5%8F%8B%E7%A9%BA%E9%97%B4%E8%AF%B4%E8%AF%B4.py)
* 爬取微博热搜榜，清除干扰代码后，转换成中文 [点击查看](https://github.com/mrlyhao/lianxi/blob/master/%E7%88%AC%E5%8F%96%E5%BE%AE%E5%8D%9A%E7%83%AD%E6%90%9C%E6%A6%9C.py)
