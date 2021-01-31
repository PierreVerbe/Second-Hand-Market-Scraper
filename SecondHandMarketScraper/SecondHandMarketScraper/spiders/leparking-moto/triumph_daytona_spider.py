import scrapy
from scrapy_splash import SplashRequest

from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

class TriumphDaytonaSpider(scrapy.Spider):
    name = 'LPM_Triumph_Daytona_Spider'

    custom_settings = {
        'DOWNLOAD_DELAY': 2,
    }

    lua_script="""

    """

    def start_requests(self):
        urls = [
            'https://www.leparking-moto.fr/moto-occasion/triumph-daytona-675-france.html#!/moto-occasion/triumph-daytona-675.html%3Ftri%3Ddate',
        ]
        for url in urls:
            yield SplashRequest(url=url, callback=self.parse, args={
                'timeout':10,
                'wait': 3,
                'lua_source': self.lua_script
                })
    

    def parse(self, response):
        data = self.parse_item

        # Works !
        self.logger.debug("hello")

        """
        for element in response.xpath('//ul[@id="resultats"]/li/section[@class="clearfix complete-holder"]/div[@class="padd-bloc clearfix"]'):
            yield {
                'price': element.xpath('div[@class="info-comp clearfix"]/div[@class="price-block "]/p/text()').get(),
            }
        """

    
        
        # Write into a file
        filename = f'lpm.json'
        with open(filename, 'wb') as f:
            #f.write(data)
            f.write(response.body)
        self.log(f'Saved file {filename}')

        """
        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
        """

    def parse_item(self, response):
        for element in response.xpath('//ul[@id="resultats"]/li/section[@class="clearfix complete-holder"]/div[@class="padd-bloc clearfix"]'):
            yield {
                'price': element.xpath('div[@class="info-comp clearfix"]/div[@class="price-block "]/p/text()').get(),
            }
     
"""
response.xpath('//ul[@id="resultats"]/li/section[@class="clearfix complete-holder"]/div[@class="padd-bloc clearfix"]/di 
   ...: v[@class="info-comp clearfix"]/div[@class="price-block "]/p/text()').getall()
   """

class test(scrapy.Spider):
    name = 'test'




# Run spiders sequentially
configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
runner = CrawlerRunner()

@defer.inlineCallbacks
def crawl():
    yield runner.crawl(TriumphDaytonaSpider)
    yield runner.crawl(test)
    reactor.stop()

crawl()
reactor.run() # the script will block here until the last crawl call is finished
