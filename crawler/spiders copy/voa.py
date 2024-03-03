from ..lib import BaseSpider

class VoaSpider(BaseSpider):
	name = "voa"
	allowed_domains = ["amharic.voanews.com"]
	start_urls = ["https://amharic.voanews.com"]
