# -*- coding: utf-8 -*-
import scrapy


class AcademicProgressRateSpider(scrapy.Spider):
    name = 'Academic_Progress_Rate'
    allowed_domains = ['mcparrish.github.io']
    start_urls = ['https://mcparrish.github.io/College_Athletics/Academic_Progress_Rate.htm']

    def parse(self, response):
        fieldnames = ['Sport', 'School', 'State', 'Academic Year', 'Multi-Year Rate', 'Penalties', 'Postseason']
        for tr in response.xpath('//*[@id="searchResultsTable"]/tbody/tr'):
            item = {}
            for i, field in enumerate(fieldnames):
                item[field] = ''.join(tr.xpath('td[{}]//text()'.format(i+1)).extract()).strip()
            yield item
