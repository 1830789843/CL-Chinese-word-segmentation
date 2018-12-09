# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.org/en/latest/topics/items.html

from scrapy import Item, Field


class ContentItem(Item):
    content = Field()
    channel = Field()
    date = Field()
    source = Field()
    editor = Field()
    keywords = Field()
    url = Field()
