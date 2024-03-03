from scrapy.item import Item, Field
# from scrapy.loader.processors import TakeFirst, MapCompose, Join
from itemloaders.processors import TakeFirst, MapCompose, Join
from w3lib.html import remove_tags
from .lib import strip_and_remove_comma



class FanabcItem(Item):
		# meta data
		url = Field(output_processor=TakeFirst())
		article_timestamp = Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
		scrap_timestamp = Field(output_processor=TakeFirst())

		title = Field(input_processor=MapCompose(remove_tags, strip_and_remove_comma), output_processor=TakeFirst(), default="")
		# headlines = Field(input_processor=MapCompose(remove_tags, strip_and_remove_comma), output_processor=Join("-"), default="")
		# tags = Field(input_processor=MapCompose(remove_tags, strip_and_remove_comma), output_processor=Join("-"), default="")
		text = Field(input_processor=MapCompose(remove_tags, strip_and_remove_comma), output_processor=Join("-"), default="")
		# time = Field(input_processor=MapCompose(remove_tags, strip_and_remove_comma), output_processor=TakeFirst(), default="")