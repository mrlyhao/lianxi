import requests
import json

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
data = {
        'from':'AUTO',
        'to':'AUTO',
        'smartresult':'dict',
        'client':'fanyideskweb',
        'doctype':'json',
        'version':'2.1',
        'keyfrom':'fanyi.web',
        'action':'FY_BY_REALTIME',
        'typoResult':'false'
        }
shuru = str(input('输入想翻译的文字'))
data['i']=shuru
r= requests.post(url,data=data)
x = json.loads(r.text)
print(x['translateResult'][0][0]['tgt'])