import datetime
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from ..items.reporter import ReporterItem


class ReporterSpider(CrawlSpider):
    name = "reporter"
    allowed_domains = ["www.ethiopianreporter.com"]
    start_urls = ["https://www.ethiopianreporter.com/"]

    rules = (
        # Rule to follow links like "https://www.ethiopianreporter.com/..." with a callback
        Rule(LinkExtractor(
            allow=r'\d+',
            deny=('page'),
        ), callback='parse_article'),

        # Rule to follow other links without a callback, excluding specific paths
        Rule(LinkExtractor(), follow=True),
    )

    def parse_article(self, response):
        loader = ItemLoader(item=ReporterItem(), response=response)


        # meta data
        loader.add_value("url", response.url)
        loader.add_css("article_timestamp", "div.tdb-block-inner.td-fix-index time.entry-date.updated.td-module-date::attr(datetime)")
        # display current time
        loader.add_value("scrap_timestamp", datetime.datetime.now())


        # title
        loader.add_css("title", "h1.tdb-title-text")

        # author
        loader.add_css('author', 'a.tdb-author-name')

        # text
        loader.add_css('text', 'div.tdb-block-inner.td-fix-index p')

        # tags
        loader.add_css('tags', 'ul.tdb-tags li a')

        yield loader.load_item()




    def closed(self, reason):
        print("spider closed")
        print(reason)
