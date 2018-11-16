# -*- coding: utf-8 -*-
import scrapy


class NcaaAprSpider(scrapy.Spider):
    name = 'NCAA_APR'
    allowed_domains = ['mcparrish.github.io']
    start_urls = ['https://mcparrish.github.io/College_Athletics/NCAA_APR.htm']

    def parse(self, response):
        for tr in response.xpath('//*[@id="coachNameTable"]/tbody/tr'):
            item = {}
            item['name'] = (tr.xpath('td/form/a/text()').extract_first() or '').strip()
            if item['name']:
                item['coachid'] = tr.xpath('td/form/input[@id="coachId"]/@value').extract_first()
                item['sport_code'] = tr.xpath('td/form/input[@id="sportCode"]/@value').extract_first()
                item['period'] = tr.xpath('td[2]/text()').extract_first().strip()
                item['school'] = tr.xpath('td[3]/text()').extract_first().strip()
                item['sport'] = tr.xpath('td[4]/text()').extract_first().strip()
                yield item
