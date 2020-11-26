# -*- coding: utf-8 -*-

BOT_NAME = 'spider'

SPIDER_MODULES = ['spiders']
NEWSPIDER_MODULE = 'spiders'

ROBOTSTXT_OBEY = False

# change cookie to yours
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'Cookie': "_T_WM=65247970278; SCF=AsNnQzoM3Op2DFePYeiLGHMnODY58DuRQa0dAEa65z835oGHJQ10ijcXoWnv8lVAEUUwg3ksTbCXQEiTPDuMvfY.; SUB=_2A25yswZEDeRhGeNO6lcQ9SbJyDWIHXVuX6oMrDV6PUJbktANLRTikW1NTw7RpiQEhwcerQY-IycZ82AFfZoNkzF3; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWgQCQR0TiH_Z9.rG86-lXT5JpX5KzhUgL.Fo-7eK-pSKnfe0.2dJLoIEXLxK-L1K5L1heLxKML1hzLBo.LxKMLBK-L1--LxKBLBo.L1hnLxK-L1K2LBKzt"}
CONCURRENT_REQUESTS = 16

DOWNLOAD_DELAY = 3

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': None,
    'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': None,
    'middlewares.IPProxyMiddleware': 100,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 101,
}

ITEM_PIPELINES = {
    'pipelines.MongoDBPipeline': 300,
}

MONGO_HOST = '127.0.0.1'
MONGO_PORT = 7001
