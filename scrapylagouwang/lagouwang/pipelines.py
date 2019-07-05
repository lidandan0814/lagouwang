# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from openpyxl import Workbook


class OpenpyxlPipeline(object):
    def __init__(self):
        self.workbook = Workbook()
        self.worksheet = self.workbook.create_sheet("lagouwang")
        self.worksheet.append(['岗位名称','工作地点', '发布时间', '薪资范围', '工作经验',
            '公司名称', '所属行业', '融资阶段', '公司规模','职位诱惑', '关键字', '学历要求'])

    def process_item(self, item, spider):
        line = [item['岗位名称'], item['工作地点'], item['发布时间'], item['薪资范围'],
            item['工作经验'], item['公司名称'], item['所属行业'], item['融资阶段'],item['公司规模'], item['职位诱惑'], item['关键字'], item['学历要求']]
        self.worksheet.append(line)
        self.workbook.save('lagouwang.xlsx')
        return item

class MongoPipeline(object):
    def __init__(self, mongo_uri, mongo_db, mongo_collection):
        self.mongo_db = mongo_db
        self.mongo_uri = mongo_uri
        self.mongo_collection = mongo_collection

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB'),
            mongo_collection=crawler.settings.get('MONGO_COLLECTION')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        self.db[self.mongo_collection].insert(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()
