# -*- coding: utf-8 -*-

# Scrapy settings for lagouwang project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'lagouwang'

SPIDER_MODULES = ['lagouwang.spiders']
NEWSPIDER_MODULE = 'lagouwang.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 6
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Language': 'en',
   'Cookie': 'JSESSIONID:ABAAABAAAGFABEFD839F56BD40011C299C61BA98384DA2A; _ga:GA1.2.407209296.1561721103;_gid:GA1.2.655437133.1561721103; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6:1561721103; user_trace_token:20190628192503-5f692005-9997-11e9-a4d0-5254005c3644; LGSID:20190628192503-5f692229-9997-11e9-a4d0-5254005c3644; PRE_UTM:; PRE_HOST:www.hao123.com; PRE_SITE:https%3A%2F%2Fwww.hao123.com%2F%3F1561345907; PRE_LAND:https%3A%2F%2Fwww.lagou.com%2F; LGUID:20190628192503-5f6923a9-9997-11e9-a4d0- 5254005c3644; index_location_city:%E5%85%A8%E5%9B%BD; TG-TRACK-CODE:index_checkmore; SEARCH_ID:498ff8c6fc7141b8834dd8e92007daa5; X_HTTP_TOKEN:23ba75965e783b20011127165193ad02d1692e8d19; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6:1561721111; LGRID:20190628192510-6405eed0-9997-11e9-bac2-525400f775ce',
   'Host': 'www.lagou.com',
   'Origin': 'https://www.lagou.com',
   'Referer': 'https://www.lagou.com/',
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.3',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'lagouwang.middlewares.LagouwangSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'lagouwang.middlewares.LagouwangDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'lagouwang.pipelines.MongoPipeline': 300,
    'lagouwang.pipelines.OpenpyxlPipeline': 301,
}

MONGO_URI = 'localhost'
MONGO_DB = 'lagou'
MONGO_COLLECTION = 'jobs'

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
