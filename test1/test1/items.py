# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import datetime
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose,TakeFirst,Join
import re

class Test1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #小说的名字
    title = scrapy.Field()
    #作者
    author = scrapy.Field()
    #小说地址
    novelurl = scrapy.Field()
    #状态
    serialstatus = scrapy.Field()
    #连载字数
    serialnumber = scrapy.Field()
    #文章类型
    category = scrapy.Field()
    #小说编号
    name_id = scrapy.Field()

    def get_insert_sql(self):#插入mysql设置
        insert_sql = """
            insert into dingdian(title, author, novelurl, serialstatus, serialnumber, category, name_id
            ) VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        params = (
            self["title"], self["author"], self["novelurl"], self["serialstatus"], self["serialnumber"],
            self["category"], self["name_id"]
        )

        return insert_sql, params