# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from test1.items import Test1Item

class XuanhuanSpider(scrapy.Spider):
    name = 'xuanhuan'
    allowed_domains = ['x23us.com']
    start_urls = ['http://www.x23us.com/class/1_1.html']

    def parse(self, response):
#        item = Test1Item()
        novelnames = response.xpath('//tr[@bgcolor="#FFFFFF"]/td[1]/a[2]/text()').extract()
        novelurls = response.xpath('//tr[@bgcolor="#FFFFFF"]/td[1]/a[1]/@href').extract()
        for i in range(len(novelnames)):
            try:
                novelname = novelnames[i]
                novelurl = novelurls[i]
                yield scrapy.Request(novelurl,callback=self.get_url,meta={'name':novelname,
                                                                           'url':novelurl})
            except:
                continue

    def get_url(self,response):
        item = Test1Item()
        item['name'] = response.meta['name']
        item['novelurl'] = response.meta['url']
        category = response.xpath('//tr/td/a/text()').extract()
        author = response.xpath('//tr[1]/td[2]/text()').extract()
        name_id = response.url[-5:]
        item['category'] = category
        item['author'] = author
        item['name_id'] = name_id
        yield item

