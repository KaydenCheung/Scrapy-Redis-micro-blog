# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


import scrapy
import pymongo
from scrapy.utils.project import get_project_settings


class WeibospiderPipeline:
    def __init__(self):
        settings = get_project_settings()
        self.connection = pymongo.MongoClient(host = settings['MONGODB_HOST'], port = settings['MONGODB_PORT'])
        db = self.connection[settings['MONGODB_DBNAME']]
        self.collection = db[settings['MONGODB_DOCNAME']]
    def process_item(self, item, spider):
        insert_data = dict(item)
        self.collection.insert(insert_data)
        return item