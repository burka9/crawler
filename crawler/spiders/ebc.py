from ..lib import BaseSpider

class EbcSpider(BaseSpider):
	name = "ebc"
	allowed_domains = ["ebc.et"]
	start_urls = ["https://ebc.et/"]
