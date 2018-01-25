#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import scrapy


class TagsSpider(scrapy.Spider):
    name = 'sf'
    allowed_domains = ['segmentfault.com']
    base_url = 'https://segmentfault.com'
    start_urls = [
        base_url + "/questions"
    ]

    def parse(self, response):
        for news in response.xpath('//section[@class="stream-list__item"]'):
            tag = [tags.xpath('.//a/@data-original-title').extract_first().strip() for tags in
                   news.xpath('.//li[@class="tagPopup"]')]
            yield {
                'title': news.xpath('.//h2//a/text()').extract_first(),
                'url': self.base_url + news.xpath('.//h2//a/@href').extract_first(),
                'author': news.xpath('.//li//a/text()').extract_first(),
                'tags': ','.join(tag),
                'view': news.xpath(
                    './/div[contains(@class,"views hidden-xs")]//span/text()').extract_first().strip(),
                'answer': news.xpath('.//div[contains(@class,"answers")]/text()').extract_first().strip()
            }

            next_page = response.xpath('//li[@class="next"]//a/@href').extract_first()
            print(next_page)
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)

    def parse2(self, response):
        for news in response.css('section.stream-list__item'):
            tag = [tags.css('a::text').extract_first().strip() for tags in news.css('li.tagPopup')]
            yield {
                'title': news.css('h2 a::text').extract_first(),
                'url': self.base_url + news.css('h2 a::attr(href)').extract_first(),
                'author': news.css('li a::text').extract_first(),
                'tags': tag
            }

            # next_page = response.css('li.next a::attr(href)').extract_first()
            # if next_page is not None:
            #     yield response.follow(next_page, callback=self.parse)
