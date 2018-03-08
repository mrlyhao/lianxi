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
login()

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