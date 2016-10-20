# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import numpy as np

class RVItem(scrapy.Item):
    price = scrapy.Field()
    location = scrapy.Field()


