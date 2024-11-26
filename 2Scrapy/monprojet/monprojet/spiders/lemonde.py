import scrapy


class LemondeSpider(scrapy.Spider):
    name = "lemonde"
    allowed_domains = ["lemonde.fr"]
    start_urls = ["https://lemonde.fr"]

    def parse(self, response):
        urls=response.css('a::attr(href)').extract()[0:9]

        absolute_urls=[response.urljoin(url) for url in urls]

        for url in absolute_urls:
            print(url)
