# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NbaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    teams = scrapy.Field()
    outcome = scrapy.Field()
    score = scrapy.Field()
    pass
