# -*- coding: utf-8 -*-

# Scrapy settings for mysql project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'testScrapy'

SPIDER_MODULES = ['testScrapy.spiders']
NEWSPIDER_MODULE = 'testScrapy.spiders'


DOWNLOAD_DELAY = 2
# DEPTH_LIMIT = 2

ITEM_PIPELINES = {
    'testScrapy.pipelines.DoubanPipeline': 301,

}

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'testScrapy.middlewares.RotateUserAgentMiddleware': 543,
}
