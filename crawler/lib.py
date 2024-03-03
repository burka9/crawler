import datetime
import re
from langid import classify
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from .items.base import BaseItem

def is_amharic(sentence):
    words = re.split(r'\W+', sentence)
    _is = 0

    for word in words:
        if classify(word)[0] == 'am':
            _is += 1

    return _is / len(words) > 0.5



items = [
	'span', 'b', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'div', 'p', 'a',
	'button', 'label', 'li', 'td', 'th', 'strong', 'em', 'i', 'u', 's',
	'small', 'big', 'code', 'pre', 'blockquote', 'q', 'cite', 'summary',
	'details', 'figcaption', 'mark', 'ins', 'del', 'sub', 'sup', 'abbr',
	'address', 'article', 'aside', 'audio', 'bdi', 'bdo', 'canvas',
	'caption', 'col', 'colgroup', 'data', 'datalist', 'dd', 'dl', 'dt',
	'fieldset', 'figure', 'footer', 'form', 'header', 'hr', 'iframe',
	'img', 'input', 'kbd', 'legend', 'main', 'map', 'meter', 'nav',
	'noscript', 'object', 'ol', 'optgroup', 'option', 'output', 'progress',
	'ruby', 'rp', 'rt', 'rtc', 'section', 'select', 'source', 'table', 'tbody',
	'textarea', 'tfoot', 'thead', 'time', 'tr', 'track', 'ul', 'var', 'video'
]


def get_text(parent):
		text = ''
		for tag in parent.css(', '.join(items)):
				data = tag.css('::text').get()

				if data is not None and is_amharic(data):
						text += data + ' '

		return text.replace('\n', ' ')



class BaseSpider(CrawlSpider):
		name = "base"
		allowed_domains = []
		selector = 'body'

		rules = (
				Rule(LinkExtractor(), follow=True, callback="parse_article"),  # follow all links
		)

		def parse_article(self, response):
				loader = ItemLoader(item=BaseItem(), response=response)

				# meta data
				loader.add_value("url", response.url)
				loader.add_value("scrap_timestamp", datetime.datetime.now())

				# text
				text = get_text(response.css(self.selector))
				loader.add_value('text', text)

				yield loader.load_item()