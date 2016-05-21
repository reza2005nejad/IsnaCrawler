# -*- coding: utf-8 -*-
from scrapy.selector import Selector
from Isna_Crawler.items import IsnaCrawlerItem
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor

import codecs


class IsnaSpider(CrawlSpider):
    name = "isna"
    allowed_domains = ["www.isna.ir"]
    start_urls = [
      "http://www.isna.ir/page/archive.xhtml?date=1395%2F02%2F04&page=1&lang=fa&pageSize=200&cerveesCode=all",
      # "http://www.asriran.com/fa/archive?service_id=-1&sec_id=-1&cat_id=-1&rpp=100&from_date=1384/01/01&to_date=1395/02/29&p=1",
      # "http://www.asriran.com/fa/archive?service_id=-1&sec_id=-1&cat_id=-1&rpp=100&from_date=1384/01/01&to_date=1395/02/29&p=2",
      # "http://www.asriran.com/fa/archive?service_id=-1&sec_id=-1&cat_id=-1&rpp=100&from_date=1384/01/01&to_date=1395/02/29&p=3",
      # "http://www.asriran.com/fa/archive?service_id=-1&sec_id=-1&cat_id=-1&rpp=100&from_date=1384/01/01&to_date=1395/02/29&p=4",
      # "http://www.asriran.com/fa/archive?service_id=-1&sec_id=-1&cat_id=-1&rpp=100&from_date=1384/01/01&to_date=1395/02/29&p=5",
    ]
    rules = [Rule(LinkExtractor(allow=('/fa/news/\d+/', )), callback='parse_item', follow=False)]



    def parse_item(self, response):
        item = IsnaCrawlerItem()
        selector  = Selector(response)
        item['titr'] = selector.xpath('//div[@class="titr"]/h1/p/text()').extract()
        item['body'] = ' '.join([x.strip() for x in (selector.xpath('//div[@class="body"]//text()').extract())])
        item['body'] = item['body'].replace('\"','').replace("\'",'').replace(u"«","").replace(u"»","").replace(",","")
        yield item
