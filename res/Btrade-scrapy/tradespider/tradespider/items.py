# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TradespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    name = scrapy.Field()
    specification = scrapy.Field()
    origin = scrapy.Field()
    image = scrapy.Field()
    price = scrapy.Field()
    unit = scrapy.Field()
    url = scrapy.Field()
