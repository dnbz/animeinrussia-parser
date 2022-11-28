#!/usr/bin/env python3
import logging
import json
import time
import os
import re

import scrapy

from scrapy.http import TextResponse
from scrapy import signals
from scrapy.utils.project import get_project_settings

from animeinrussia_parser.items import load_show

class AirSpider(scrapy.Spider):
    name = "air-spider"

    baseurl = get_project_settings().get("BASEURL")

    start_urls = [baseurl]

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(AirSpider, cls).from_crawler(crawler, *args, **kwargs)

        # Запуск функции open_spider при инициализации
        crawler.signals.connect(spider.open_spider, signal=signals.spider_opened)

        return spider

    def open_spider(self):
        # количество карточек из списков
        self.crawler.stats.set_value("total_card_items", 0)
        self.crawler.stats.set_value("db_added_items", 0)

    def parse(self, response):
        cards = response.css("section.releases .item")

        for card in cards:
            detail_path = card.xpath("./@href").get()
            detail_url = f"{self.baseurl}{detail_path}"

            # card_data = self.parse_card(card)

            yield scrapy.Request(url=detail_url, callback=self.parse_detail)

    def parse_detail(self, response):
        data = {}

        data['source_url'] = response.url

        data['pub_date'] = response.xpath("//div[@class='movie-info']/time/text()").get()

        data['title_orig'] = response.xpath("//p[@class='title-orig']/text()").get()

        data['title_ru'] = response.xpath("//div[@class='movie-info']/h2/text()").get()

        data['description'] = response.xpath("//div[@class='movie-info']/p[last()]/text()").get()

        cover_style = response.xpath("//div[@class='movie-cover']/img/@style").get()

        if cover_style:
            data['image_url'] = self.parse_bgimg(cover_style)


        item = load_show(data)
        yield item

    def parse_card(self, card: TextResponse):
        data = {}

        detail_url = card.xpath("./@href").get()

        if detail_url:
            data['detail_url'] = f"{self.baseurl}{detail_url}"

        card_style = card.xpath("./@style").get()

        if card_style:
            data['background_image'] = self.parse_bgimg(card_style)

        data['date'] = card.xpath("//time/text()").get()

        data['name_orig'] = card.xpath("./div[@class='item-info']/p/text()").get()
        data['name_ru'] = card.xpath("./div[@class='item-info']/h3/text()").get()

        return data


    def parse_bgimg(self, style: str) -> str | None:
        pattern = 'background-image:url\((.+?)\)'

        res = re.findall(pattern, style)

        if len(res) > 0:
            return f"{self.baseurl}{res[0]}"
        else:
            return None
