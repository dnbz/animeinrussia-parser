# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import logging

# useful for handling different item types with a single interface
from .db import engine, shows
from .items import show_db_format

logging.basicConfig(format="%(asctime)s %(levelname)s:%(message)s", level=logging.INFO)


class AnimeinrussiaParserPipeline:
    def open_spider(self, spider):
        self.engine = engine

    def process_item(self, item, spider):
        if item.get('source_url') is None:
            return item

        with self.engine.connect() as conn:
            show_find_stmt = shows.select().where(shows.c.source_url == item['source_url'])

            show = conn.execute(show_find_stmt).first()

            if show:
                logging.info(f"Item {item['source_url']} is already in DB. Skipping...")
                return item

            show_data = show_db_format(item)
            stmt = shows.insert().values(show_data)
            conn.execute(stmt)

        return item
