# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class ImageItem(Item):
    collection = table = 'images'  # 对应到MongoDB中的collection和MySQL中的table(名字)
    id = Field()   # 图片id
    url = Field()  # 链接
    title = Field()  # 标题
    thumb = Field()  #缩略图
