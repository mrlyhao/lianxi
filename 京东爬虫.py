import requests
from bs4 import BeautifulSoup
import time
import csv
def jd_spider(shangpin,number):
    referer = 'https://search.jd.com/Search?keyword={}&enc=utf-8&suggest=1.his.0.0&wq='.format(shangpin.encode('utf-8'))#设置引用页面，用以调用API
    headers = {'Referer':referer}
    csvFile = open('D:/shuju.csv','w+',newline='')#打开CSV文件
    try:
        write = csv.writer(csvFile)
        write.writerow(('名称','价格','评论数','店铺','链接'))#填写表头
        for i in range(1,number):
            #京东API接口，京东现在每页60个商品，ajax加载30个，调用的就是下方接口
            url1 = 'https://search.jd.com/s_new.php?keyword={}&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&suggest=1.his.0.0&page={}&s={}&click=0'.format(shangpin,i,30*i)
            a= requests.get(url1,headers = headers).text#解析页面
            soup = BeautifulSoup(a,'html.parser')
            items = soup.select('li.gl-item')#定位每一个商品
            for item in items:
                try:
                    item_url = 'http:' + item.find('div',class_="p-name").find('a')['href']#商品链接
                    sku =item['data-sku']#商品编号
                    price_url = 'http://p.3.cn/prices/mgets?skuIds=J_' + str(sku)#商品价格API接口
                    price = requests.get(price_url).json()[0]['p']#解析API
                    name = item.select('div a[target="_blank"] > em')[0].text#商品名称
                    pinglunshu = item.find('div', class_="p-commit").find('a').string#商品评论数量
                    dianpu = item.select('div[class="p-shop"] span a')[0].text#店铺名称
                    write.writerow((name,price,pinglunshu,dianpu,item_url))#逐行写入表格
                except:
                    continue
            time.sleep(0.5)
    finally:
        csvFile.close()
    print("Done")
if __name__ == "__main__":
    jd_spider('机械键盘',3)