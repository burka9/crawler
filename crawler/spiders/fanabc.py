import scrapy
import datetime
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from ..items.fanabc import FanabcItem


denyList = ["afaanoromoo", "tigrigna", "english", "arabic"]


class FanabcSpider(CrawlSpider):
    name = "fanabc"
    allowed_domains = ["www.fanabc.com"]
    start_urls = ["https://www.fanabc.com/"]
    
    rules = (
        # Rule to follow links like "https://www.fanabc.com/archives/..." with a callback
        Rule(LinkExtractor(allow=r'/archives/\d*$'), callback='parse_article'),

        # Rule to follow other links without a callback, excluding specific paths
        Rule(LinkExtractor(deny=('afaanoromoo', 'tigrigna', 'english', 'arabic')), follow=True),
    )


    def parse_article(self, response):
        loader = ItemLoader(item=FanabcItem(), response=response)
        
        
        # meta data
        loader.add_value("url", response.url)
        loader.add_css("article_timestamp", "article time b")
        # display current time
        loader.add_value("scrap_timestamp", datetime.datetime.now())


        # title
        loader.add_css("title", "article span.post-title")

        # text
        loader.add_css("text", "article div.entry-content p")
        

        yield loader.load_item()
