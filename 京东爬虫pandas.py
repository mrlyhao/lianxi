import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
headers = {'Referer':'https://search.jd.com/Search?keyword=%E6%9C%BA%E6%A2%B0%E9%94%AE%E7%9B%98&enc=utf-8&suggest=1.his.0.0&wq=&pvid=35d49cfc80334188883e02884bb55865',}
data = {}
item_urls = []
prices = []
names = []
pinglunshus = []
dianpus =[]
for i in range(1,11):
    url1 = 'https://search.jd.com/s_new.php?keyword=机械键盘&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&suggest=1.his.0.0&page={}&s={}&click=0'.format(i,30*i)
    a= requests.get(url1,headers = headers).text
    soup = BeautifulSoup(a,'html.parser')
    items = soup.select('li.gl-item')
    for item in items:
        try:
            item_url = 'http:' + item.find('div',class_="p-name").find('a')['href']
            sku =item['data-sku']
            price_url = 'http://p.3.cn/prices/mgets?skuIds=J_' + str(sku)
            price = requests.get(price_url).json()[0]['p']
            name = item.select('div a[target="_blank"] > em')[0].text
            pinglunshu = item.find('div', class_="p-commit").find('a').string
            dianpu = item.select('div[class="p-shop"] span a')[0].text
            item_urls.append(item_url)
            prices.append(price)
            names.append(name)
            pinglunshus.append(pinglunshu)
            dianpus.append(dianpu)
        except:
            continue
data['名称'] = names
data['价格'] = prices
data['评论数'] = pinglunshus
data['店铺'] = dianpus
data['链接'] = item_urls
print(data)
df = pd.DataFrame(data)
df.to_csv('京东商品数据.csv',mode='a',encoding="gb2312")
print("Done")
