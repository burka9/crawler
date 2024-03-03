import datetime
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from ..items.wikipedia import WikipediaItem
from ..lib import get_text


class WikipediaSpider(CrawlSpider):
    name = "wikipedia"
    allowed_domains = ["am.wikipedia.org"]
    start_urls = ["https://am.wikipedia.org/"]

    rules = (
        Rule(LinkExtractor(), follow=True, callback="parse_article"),  # follow all links
    )

    def parse_article(self, response):
        loader = ItemLoader(item=WikipediaItem(), response=response)

        # meta data
        loader.add_value("url", response.url)
        loader.add_value("scrap_timestamp", datetime.datetime.now())

        text = get_text(response.css('main#content'))

        # text
        loader.add_value('text', text)

        yield loader.load_item()
