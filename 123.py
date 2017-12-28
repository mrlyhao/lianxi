import requests

url = 'http://www.baidu.com/'
proxies = {"http":"http://112.114.95.179:8118"}
a = requests.post(url,proxies = proxies)
print(a)
