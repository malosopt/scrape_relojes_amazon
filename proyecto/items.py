# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProyectoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # PRIMARY FIELDS
    title = Field()
    price = Field()

    # CALCULATED FIELDS
    images = Field()
    location = Field()

    # HOUSEKEEPING FIELDS
    url = Field()
    project = Field()
    server = Field()
    spider = Field()
    date = Field()