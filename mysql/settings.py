# -*- coding: utf-8 -*-

# Scrapy settings for mysql project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'mysql'

SPIDER_MODULES = ['mysql.spiders']
NEWSPIDER_MODULE = 'mysql.spiders'


DOWNLOAD_DELAY = 2
# DEPTH_LIMIT = 2

ITEM_PIPELINES = {
    'mysql.pipelines.DoubanPipeline': 301,

}

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'mysql.middlewares.RotateUserAgentMiddleware': 543,
}
