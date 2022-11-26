import string
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider


class ConcordiaSpider(scrapy.Spider):
    totalLimit = 10
    name = "Concordia"
    allowed_domains = ["concordia.ca"]
    start_urls = ["https://www.concordia.ca/ginacody/"]
    visited_urls = set()
    rules = (
        Rule(
            LinkExtractor(),
            callback='parse_item',
            follow=True),
    )
    custom_settings = {
        'CONCURRENT_REQUESTS': 10,
        'ROBOTSTXT_OBEY': True,
        'FEED_FORMAT': 'json',
        'FEED_URI': 'output.json',
        'OVERWRITE': True
    }

    def parse(self, response):
        print("Processing:" + response.url)
        # prevent french pages from interfering with all other aspects of the program
        language = response.xpath('/html/@lang').extract_first()

        if language == 'en':
            if response.url in self.visited_urls:
                return
            self.visited_urls.add(response.url)
            if len(self.visited_urls) > self.totalLimit:
                raise CloseSpider('page_limit_exceeded')

            else:
                yield {
                    "title": response.xpath('//title/text()').extract_first(),
                    'url': response.url,
                    'html': response.text,
                }
        for link in LinkExtractor().extract_links(response):
            yield scrapy.Request(link.url, callback=self.parse)
