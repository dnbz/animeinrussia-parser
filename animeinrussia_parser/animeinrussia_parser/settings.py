from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime
import os

load_dotenv()

# custom settings
BASEURL = "https://animeinrussia.ru"

DB_CONNECTION = os.environ.get(
    "DB_CONNECTION", "postgresql://user:password@127.0.0.1:5432/parser"
)


DEBUG_SAVE_DIR = Path.cwd() / "debug"


# scrapy settings
LOG_LEVEL = os.environ.get("LOG_LEVEL", "DEBUG")
STDOUT_LOG = bool(os.environ.get("STDOUT_LOG", False))
if not STDOUT_LOG:
    LOG_FILE = Path.cwd() / (
        "logs/" + datetime.now().strftime("%Y-%m-%d") + "_parser.log"
    )

# feeds to save data
feed_file = DEBUG_SAVE_DIR / (datetime.now().strftime("%Y-%m-%d") + "_feed.json")
FEEDS = {
    f"{feed_file}": {
        "format": "json",
        "encoding": "utf8",
        "store_empty": False,
        "indent": 4,
        "item_export_kwargs": {
            "export_empty_fields": True,
        },
    }
}

ITEM_PIPELINES = {
   'animeinrussia_parser.pipelines.AnimeinrussiaParserPipeline': 300,
}


# FEED_FORMAT = "json"
# FEED_URI = DEBUG_SAVE_DIR / (datetime.now().strftime("%Y-%m-%d") + "_listings.json")


# AutoThrottle. See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = False


# HttpCache. See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 3600
HTTPCACHE_DIR = "httpcache"
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"


BOT_NAME = "animeinrussia_parser"

SPIDER_MODULES = ["animeinrussia_parser.spiders"]
NEWSPIDER_MODULE = "animeinrussia_parser.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'animeinrussia_parser (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'animeinrussia_parser.middlewares.AnimeinrussiaParserSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'animeinrussia_parser.middlewares.AnimeinrussiaParserDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
