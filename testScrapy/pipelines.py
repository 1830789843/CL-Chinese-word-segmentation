# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import log

from mysql import settings
from mysql.items import ContentItem


class DoubanPipeline(object):
    def __init__(self):
        self.counter = 0;

    def process_item(self, item, spider):
        # print('process_item')

        # filename = '/home/admin/scrapy/mysql/spiders/data/' +str(self.counter).zfill(4) + '.txt'
        filename = './data/raw/' +str(self.counter).zfill(4) + '.txt'

        f = open(filename, 'w')
        print(item['content'])
        f.write(item['content'])
        f.close()

        with open('./data/channel.txt', 'a+') as f:
            f.writelines(str(self.counter)+'\t'+item['channel']+'\n')
        with open('./data/date.txt', 'a+') as f:
            f.writelines(str(self.counter)+'\t'+item['date']+'\n')
        with open('./data/editor.txt', 'a+') as f:
            f.writelines(str(self.counter)+'\t'+item['editor']+'\n')
        with open('./data/keywords.txt', 'a+') as f:
            f.writelines(str(self.counter)+'\t'+item['keywords']+'\n')
        with open('./data/source.txt', 'a+') as f:
            f.writelines(str(self.counter)+'\t'+item['source']+'\n')
        with open('./data/url.txt', 'a+') as f:
            f.writelines(str(self.counter)+'\t'+item['url']+'\n')

        self.counter += 1
        print(filename)
