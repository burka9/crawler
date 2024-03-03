from scrapy.item import Item, Field
from itemloaders.processors import TakeFirst, MapCompose, Join
from w3lib.html import remove_tags
from .lib import strip_and_remove_comma


class BaseItem(Item):
  # meta data
	url = Field(output_processor=TakeFirst())
	scrap_timestamp = Field(output_processor=TakeFirst())

	text = Field(input_processor=MapCompose(remove_tags, strip_and_remove_comma), output_processor=Join(" "), default="")
