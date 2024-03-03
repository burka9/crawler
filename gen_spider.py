from sys import argv
from urllib.parse import urlparse

template = """from ..lib import BaseSpider

class {class_name}(BaseSpider):
	name = "{spider_name}"
	allowed_domains = ["{domain}"]
	start_urls = ["{start_url}"]
"""



def gen_spider(spider_name, start_url):
	class_name = spider_name.capitalize() + "Spider"
	parsed_url = urlparse(f"https://{start_url}") if start_url.startswith("https://") is False else urlparse(start_url)
	domain = parsed_url.netloc
	start_url = parsed_url.geturl()
	data = template.format(class_name=class_name, spider_name=spider_name, domain=domain, start_url=start_url)

	# save file to crawler/spiders/{spider_name}.py
	with open(f"spiders/{spider_name}.py", "w") as f:
		f.write(data)

	return f"crawler/spiders/{spider_name}.py"


if len(argv) != 3:
	print("Usage: gen_spider.py <spider_name> <start_url>")
	exit(1)

# args: spider_name, start_url
gen_spider(argv[1], argv[2])