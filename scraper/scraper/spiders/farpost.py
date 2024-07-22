import scrapy


class FarpostSpider(scrapy.Spider):
    name = "farpost"
    allowed_domains = ["www.farpost.ru"]
    start_urls = [
        "https://www.farpost.ru/vladivostok/service/construction/guard/+/Системы+видеонаблюдения/"
    ]

    # def parse_author(self, response):
    #     return response.css('span.userNick a::text').get()

    def parse(self, response):
        for index, add in enumerate(response.css('tbody tr'), start=0):
            if add.css('td div div div div div a::text').get() is not None:
                if index <= 10:
                    yield {
                        "title": add.css('td div div div div div a::text').get(),
                        "add_id": add.css('td div div a::attr(name)').get(),
                        "views_count": add.css('span::text').get(),
                        "position": index
                    }
                else:
                    break
            else:
                continue
