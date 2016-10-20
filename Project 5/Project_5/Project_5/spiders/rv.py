# -*- coding: utf-8 -*-
import scrapy
from Project_5.items import RVItem

class RvSpider(scrapy.Spider):
    name = "rv"
    cities = ["newyork","losangeles","chicago","houston", "philadelphia","phoenix","sanantonio","sandiego","dallas", "sfbay"]
    city_urls = ["http://%s.craigslist.org/search/rva" % city for city in cities]
    start_urls = city_urls

    def parse(self, response):
        prices = response.xpath("//span/span[@class='price']/text()").extract()
        location = response.url.split('.')[0][7:]

        for price in prices:
            item = RVItem()
            item['price'] = int(price[1:])
            item['location'] = location
            yield item

        next_page_url = response.xpath("//a[@class='button next']/@href").extract_first()
        if next_page_url:
            abs_next_page_url = response.urljoin(next_page_url)
            request = scrapy.Request(url=abs_next_page_url)
            yield request


