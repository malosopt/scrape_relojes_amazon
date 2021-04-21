import scrapy
from proyecto.items import ProyectoItem

class BasicSpider(scrapy.Spider):
    name = 'basic'
    #allowed_domains = ['amazon]
    start_urls = ['https://www.amazon.com/dp/B003MYYJD0/']

    def parse(self, response):
        
        item = ProyectoItem()
        item['title'] = response.xpath('//h1/text()').extract()
        return item
