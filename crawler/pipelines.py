# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os
from itemadapter import ItemAdapter
from pymongo import MongoClient
from dotenv import load_dotenv
from scrapy.exceptions import DropItem

load_dotenv()


mongo_uri = os.getenv("MONGO_URI")
username = os.getenv("MONGO_USERNAME")
password = os.getenv("MONGO_PASSWORD")


class DatabasePipeline:
    def __init__(self):
        try:
            self.client = MongoClient(mongo_uri, username=username, password=password)
            self.db = self.client["crawler"]
            self.collection = {}

            # bbc collection
            self.collection["bbc"] = self.db["bbc"]
            self.collection["bbc"].create_index("url", unique=True)
            
            # fanabc collection
            self.collection["fanabc"] = self.db["fanabc"]
            self.collection["fanabc"].create_index("url", unique=True)
            
            # reporter collection
            self.collection["reporter"] = self.db["reporter"]
            self.collection["reporter"].create_index("url", unique=True)

            # wikipedia collection
            self.collection["wikipedia"] = self.db["wikipedia"]
            self.collection["wikipedia"].create_index("url", unique=True)
        except Exception as ex:
            print(ex)
    
    def process_item(self, item, spider):
        if spider.name == "bbc":
            self.process_bbc_item(item, self.collection["bbc"])
        elif spider.name == "fanabc":
            self.process_fanabc_item(item, self.collection["fanabc"])
        elif spider.name == "reporter":
            self.process_reporter_item(item, self.collection["reporter"])
        elif spider.name == "wikipedia":
            self.process_wikipedia_item(item, self.collection["wikipedia"])
        elif spider.name == "base":
            return DropItem("Dropped")
        else:
            self.process_base_item(item, spider.name)

        return item

    def process_base_item(self, item, collection_name):
        try:
            # collection
            self.collection[collection_name] = self.db[collection_name]
            self.collection[collection_name].create_index("url", unique=True)
        except:
            pass
        
        try:
            self.collection[collection_name].insert_one(dict(
                url="" if "url" not in item else item["url"],
                scrap_timestamp="" if "scrap_timestamp" not in item else item["scrap_timestamp"],
                text="" if "text" not in item else item["text"],
            ))
        except Exception as ex:
            print(ex)

    def process_bbc_item(self, item, collection):
        try:
            collection.insert_one(dict(
                url="" if "url" not in item else item["url"],
                article_timestamp="" if "article_timestamp" not in item else item["article_timestamp"],
                scrap_timestamp="" if "scrap_timestamp" not in item else item["scrap_timestamp"],
                title="" if "title" not in item else item["title"],
                headlines="" if "headlines" not in item else item["headlines"],
                tags="" if "tags" not in item else item["tags"],
                text="" if "text" not in item else item["text"],
                time="" if "time" not in item else item["time"],
            ))
        except Exception as ex:
            print(ex)
            
    def process_fanabc_item(self, item, collection):
        try:
            collection.insert_one(dict(
                url="" if "url" not in item else item["url"],
                article_timestamp="" if "article_timestamp" not in item else item["article_timestamp"],
                scrap_timestamp="" if "scrap_timestamp" not in item else item["scrap_timestamp"],
                title="" if "title" not in item else item["title"],
                text="" if "text" not in item else item["text"],
            ))
        except Exception as ex:
            print(ex)

    def process_reporter_item(self, item, collection):
        try:
            collection.insert_one(dict(
                url="" if "url" not in item else item["url"],
                article_timestamp="" if "article_timestamp" not in item else item["article_timestamp"],
                scrap_timestamp="" if "scrap_timestamp" not in item else item["scrap_timestamp"],
                title="" if "title" not in item else item["title"],
                author="" if "author" not in item else item["author"],
                tags="" if "tags" not in item else item["tags"],
                text="" if "text" not in item else item["text"],
            ))
        except Exception as ex:
            print(ex)

    def process_wikipedia_item(self, item, collection):
        try:
            collection.insert_one(dict(
                url="" if "url" not in item else item["url"],
                scrap_timestamp="" if "scrap_timestamp" not in item else item["scrap_timestamp"],
                text="" if "text" not in item else item["text"],
            ))
        except Exception as ex:
            print(ex)