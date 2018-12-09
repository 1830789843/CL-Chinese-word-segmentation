# coding:utf-8

from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from mysql.items import ContentItem
from mysql import settings

from scrapy import log
from scrapy.link import Link
from scrapy.http.response import Response

import re
import datetime

class ContentSpider(CrawlSpider):

    name = 'content'
    allowed_domains = ['sina.com.cn']


    start_urls = ['http://news.sina.com.cn/',
                  ]
    rules = (
             Rule(LinkExtractor(allow=r".*doc[^/]*shtml$"), callback='parse_content', follow=True),
             )


    def parse_content(self, response):

        print(response.url)
        try:
            item = ContentItem()

            article = response.selector.xpath('//*[@class="article"]')
            if len(article)==0:
                return
            a = article[0].xpath('./p/text()').extract()

            b = ''
            for i, str in enumerate(a):
                if i >=len(a)-2:
                    if str.find(u'责任编辑：')!=-1:
                        item['editor'] = str.replace(u'责任编辑：','')
                        continue;
                    else:
                        pattern = re.compile(r'（[\u4e00-\u9fa5]+）')
                        result = pattern.findall(str)
                        if len(result)>0:
                            item['editor'] = result[0]
                        continue;

                b += ''.join(str.split())
                # b += '\n'

            item['content'] = b

            if 'editor' not in item.values():
                item['editor'] = 'None'

            channel = response.selector.xpath('//*[@class="channel-path"]')
            a = channel[0].xpath('./a/text()').extract()
            b = a[0]
            b.replace(u'新浪', '')
            item['channel'] = b

            date_source = response.selector.xpath('//*[@class="date-source"]')
            date = date_source[0].xpath('./span/text()').extract()
            item['date'] = re.compile(r'\d+年\d+月\d+日').findall(date[0])[0]

            source = date_source[0].xpath('./a/text()').extract()
            if len(source)==0:
                item['source'] = 'None'
            else:
                item['source'] = source[0]

            keywords = response.selector.xpath('//*[@class="keywords"]')
            if len(keywords)>0:
                a = keywords[0].xpath('./a/text()').extract()
                item['keywords'] = ' '.join(a)
            else:
                item['keywords'] = 'None'

            item['url'] = response.url

            print(item)
            yield item

        except Exception as error:
            log(error)

