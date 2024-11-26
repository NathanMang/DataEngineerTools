import scrapy

class ChurchillQuotesSpider(scrapy.Spider):
    name = "citations de Churchill"
    start_urls = ["http://evene.lefigaro.fr/citations/winston-churchill",]

    def parse(self, response):
        for cit in response.xpath('//div[@class="figsco__quote__text"]'):
            text_value = cit.xpath('a/text()').extract_first()

            #Supprimer les quillemets
            text_value=text_value.replace("“", "").replace("”", "").strip()

             # Récupérer le nom de l'auteur
            author_name = cit.xpath('//div[@class="figsco__fake__col-9"]/a/text()').extract_first()

            if author_name =="Winston Churchill":
                yield { 'text' : text_value,
                        'author': author_name
                }

            
