# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import dateparser
from datetime import datetime
from itemloaders.processors import Join, MapCompose, TakeFirst, Identity
from scrapy.utils.project import get_project_settings

from scrapy.loader import ItemLoader

def time_now():
    return datetime.now().replace(microsecond=0)

def load_show(data: dict):
    loader = ShowLoader(item={})

    for key in data:
        loader.add_value(key, data[key])

    item = loader.load_item()

    return item

def show_db_format(show: dict):
    data = show.copy()

    if data.get("pub_date"):
        data["pub_date"] = dateparser.parse(data["pub_date"])

    t = time_now()

    data['created_at'] = t
    data['updated_at'] = t

    return data


class ShowLoader(ItemLoader):
    default_input_processor = MapCompose(str.split)
    default_output_processor = Join()
