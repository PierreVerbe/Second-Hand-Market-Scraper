import scrapy
import logging

class TriumphDaytonaSpider(scrapy.Spider):
    name = 'Triumph_Daytona_Spider'
    start_urls = [
        'https://www.leboncoin.fr/recherche?category=3&moto_brand=triumph&moto_model=Daytona&regdate=2005-max',
    ]

    def parse(self, response):
        logging.log(logging.WARNING, "This is a warning")
        print(response.xpath('/html/body/div[2]/div/section/main/div/div[1]/div[6]/div/div[5]/div[1]/div[1]'))
        for quote in response.xpath('/html/body/div[2]/div/section/main/div/div[1]/div[6]/div/div[5]/div[1]/div[1]'):
            yield {
                'title': quote.xpath('/html/body/div[2]/div/section/main/div/div[1]/div[6]/div/div[5]/div[1]/div[1]/div[7]/a/div/div/div/div[1]/div[2]/div[1]/div[1]/div[1]/p').get(),
                'price': quote.xpath('/html/body/div[2]/div/section/main/div/div[1]/div[6]/div/div[5]/div[1]/div[1]/div[7]/a/div/div/div/div[1]/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/span/span').get(),
            }

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
            