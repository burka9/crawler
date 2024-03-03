import scrapy
import datetime
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from ..items.bbc import BBCItem


class BbcSpider(CrawlSpider):
    name = "bbc"
    allowed_domains = ["www.bbc.com"]
    start_urls = ["https://bbc.com/amharic"]
    
    rules = (
        Rule(LinkExtractor(
            allow=("topics")
        ), follow=True),
        Rule(LinkExtractor(
            allow=("articles"),
        ), callback="parse_article", follow=True)
    )

    def parse_article(self, response):
        loader = ItemLoader(item=BBCItem(), response=response)
        

        # meta data
        loader.add_value("url", response.url)
        loader.add_css("article_timestamp", "main time::attr(datetime)")
        # display current time
        loader.add_value("scrap_timestamp", datetime.datetime.now())


        # title
        loader.add_css("title", "h1")
        
        # headlines
        loader.add_css("headlines", "main h2")
        
        # text
        loader.add_css("text", "main p")
        
        # tags
        loader.add_css("tags", "aside ul li a")
        
        # time
        loader.add_css("time", "main time")

        
        yield loader.load_item()

    
    def closed(self, reason):
        print("spider closed")
        print(reason)
