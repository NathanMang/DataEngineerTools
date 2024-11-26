import scrapy


class Lemondev3Spider(scrapy.Spider):
    name = "lemondev3"
    allowed_domains = ["lemonde.fr"]
    start_urls = ["https://lemonde.fr"]

    def parse(self, response):
        pass
