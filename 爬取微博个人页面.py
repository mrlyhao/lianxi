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

# 打开一个session后续操作继承cookie
session = requests.Session()

def login(username,password):
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
        # print(session.cookies)
        # print(final)
    except BaseException as e:
        print(e)
def parse(uid):
    #设置referer和headers
    Referer='https://m.weibo.cn/u/{}'.format(uid)
    headers_1 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
        "Referer":Referer
    }
    #使用firefox抓包工具抓取真实的地址，并分析参数，需要设置UID和page
    for i in range(1,11):
        url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value={}&containerid=107603{}&page={}'.format(uid,uid,i)
        #抓取页面后将json转换成dic并提取信息
        webdata = session.get(url, headers=headers_1).text
        data = json.loads(webdata)
        news = data['data']['cards']
        for new in news:
            try:
                info = new['mblog']['text']
                #替换所有的HTML标签
                import re
                dr = re.compile(r'\<.*?\>', re.S)
                dd = dr.sub('', info)
                print(dd)
            except BaseException as e:
                print(e)
login(username='liyuanhaode@sina.cn',password='****')
parse('1173544654')

