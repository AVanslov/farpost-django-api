from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class FarpostSpider(CrawlSpider):
    name = "farpost_author"
    allowed_domains = ["www.farpost.ru"]
    start_urls = [
        "https://www.farpost.ru/vladivostok/service/construction/guard/+/Системы+видеонаблюдения/"
    ]

    rules = (
        Rule(
            LinkExtractor(
                restrict_css='tbody tr td div div a'
            ),
            callback='parse_item'
        ),
    )

    def parse_item(self, response):
        yield {
            "author": response.css('span.userNick a::text').get()
        }
