# coding=gbk
import urllib2
import urllib

url = 'http://ad.shucong.com/admin/union/users'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
values = {'username':'李元昊','password':'123456'}
headers = {'User-Agent':'user_agent'}
data = urllib.urlencode(values)
request = urllib2.Request(url,data,headers)
response = urllib2.urlopen(request)
page= response.read()
print page
