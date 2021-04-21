# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProyectoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # PRIMARY FIELDS
    title = scrapy.Field()
    #price = scrapy.Field()

    # CALCULATED FIELDS
    #images = scrapy.Field()
    #location = scrapy.Field()

    # HOUSEKEEPING FIELDS
    #url = scrapy.Field()
    #project = scrapy.Field()
    #server = scrapy.Field()
    #spider = scrapy.Field()
    #date = scrapy.Field()