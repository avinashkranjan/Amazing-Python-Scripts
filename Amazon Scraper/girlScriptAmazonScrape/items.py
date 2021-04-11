# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GirlscriptamazonscrapeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name =scrapy.Field()
    price = scrapy.Field()
    author = scrapy.Field()
    image_link= scrapy.Field()