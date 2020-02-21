# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import re
import logging

class YangguangPipeline(object):
    def process_item(self, item, spider):
        item["content"] = self.process_content(item["content"])
        logging.warning(item)
        return item

    def process_content(self, context):
        content = [re.sub(r"\xa0|\s", "", i) for i in context]
        content = [i for i in content if len(i) > 0]
        return content
