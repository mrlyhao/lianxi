import re
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from test1.items import Test1Item

class Myspider(scrapy.Spider):
    name = 'dingdian'
    allowed_domains = ['23us.so']
    bash_url = 'http://www.23us.so/list/'
    bashurl = '.html'
    def start_requests(self):
        for i in range(1,11):
            url = self.bash_url + str(i) +'_1' + self.bashurl
            yield Request(url,self.parse)

    def parse(self, response):
        max_num = response.css('a[class = "last"]::text').extract()[0]
        bashurl = str(response.url)[:-6]
        for num in range(1,int(max_num)+1):
                url = bashurl + str(num) + self.bashurl
                yield Request(url,callback=self.get_name)

    def get_name(self,response):
        novelnames = response.xpath('//tr[@bgcolor="#FFFFFF"]/td[1]/a[1]/text()').extract()
        novelurls = response.xpath('//tr[@bgcolor="#FFFFFF"]/td[1]/a[1]/@href').extract()
        for i in range(len(novelnames)):
            try:
                novelname = novelnames[i]
                novelurl = novelurls[i]
                yield  Request(novelurl,callback=self.get_chapterurl,meta={'name':novelname,
                                                                           'novelurl':novelurl})
            except:
                continue

    def get_chapterurl(self,response):
        item = Test1Item()
        item['title'] = response.meta['name']
        item['novelurl'] = response.meta['novelurl']
        serialstatus=response.xpath('//table[@id="at"]/tr[1]/td[3]/text()').extract()[0]
        serialnumber=response.xpath('//tr[2]/td[2]/text()').extract()[0].replace('&nbsp;','')
        category = response.xpath('//tr/td/a/text()').extract()[0]
        author = response.xpath('//tr[1]/td[2]/text()').extract()[0]
        name_id = response.url.split('/')[-1][:-5]
        item['serialstatus'] = serialstatus
        item['serialnumber'] = serialnumber
        item['category'] = category
        item['author'] = author
        item['name_id'] = name_id
        yield item
