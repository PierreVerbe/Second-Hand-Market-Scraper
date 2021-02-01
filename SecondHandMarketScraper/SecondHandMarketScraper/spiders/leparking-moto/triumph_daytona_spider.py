import scrapy
from scrapy_splash import SplashRequest

from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

import json

class LPMTriumphDaytonaLinksSpider(scrapy.Spider):
    name = 'LPM_Triumph_Daytona_Links_Spider'
    base_url = 'https://www.leparking-moto.fr'
    custom_settings = {
        'DOWNLOAD_DELAY': 3,
        'COOKIES_ENABLED': False,
    }

    lua_script="""
        function main(splash, args)
            assert(splash:go(args.url))
            assert(splash:wait(5))
            return {
                html = splash:html(),
            }
        end
    """

    def start_requests(self):
        urls = [
            'https://www.leparking-moto.fr/moto-occasion/triumph-daytona-675.html#!/moto-occasion/triumph-daytona-675.html%3Fslider_millesime%3D2013%7C2021%26tri%3Ddate',
        ]
        for url in urls:
            yield SplashRequest(url=url, callback=self.parse, args={
                'timeout':10,
                'wait': 3,
                'lua_source': self.lua_script
                })

    def parse(self, response):
        links = self.parse_links(response)

        # Write into a file
        filename = f"SecondHandMarketScraper/SecondHandMarketScraper/resources/leparking-moto/LPM_Triumph_Daytona_Links.json"

        f = open(filename, "w")
        for l in links:
            complete_links = {'links': list(map(lambda x: self.base_url + x, l["links"]))}
            resultString = json.dumps(complete_links, indent=4)
            f.write(resultString)
        #f.write(response.body)
        f.close()

        self.logger.debug(f"Saved file {filename}")

        """
        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
        """

    def parse_links(self, response):
        for element in response.xpath('//ul[@id="resultats"]'):
            yield {
                'links': element.xpath('//a[@class="external btn-plus "]/@href').getall(),
            }
     
class LPMTriumphDaytonaSalesSpider(scrapy.Spider):
    name = 'LPM_Triumph_Daytona_Sales_Spider'

    custom_settings = {
        'DOWNLOAD_DELAY': 3,
        'COOKIES_ENABLED': False,
    }

    lua_script="""
    
    """

    def start_requests(self):
        urls = [
            'https://www.leparking-moto.fr//moto-occasion-detail/triumph-daytona-daytona-675/triumph-daytona-675-noir/3234HL1.html',
        ]
        for url in urls:
            yield SplashRequest(url=url, callback=self.parse, args={
                'timeout':10,
                'wait': 3,
                'lua_source': self.lua_script
                })

    def parse(self, response):
        moto = self.parse_links(response)

        # Write into a file
        filename = f"SecondHandMarketScraper/SecondHandMarketScraper/resources/leparking-moto/LPM_Triumph_Daytona_Results.json"

        f = open(filename, "w")
        for m in moto:
            resultString = json.dumps(m, indent=4)
            f.write(resultString)
            f.write("\n")
        f.close()
        
        self.logger.debug(f"Saved file {filename}")

    def parse_links(self, response):
        for element in response.xpath('//section[@class="top-detail clearfix"]'):
            yield {
                'name': element.xpath('//span[@itemprop="name"]/text()').getall(),
                'published': element.xpath('//span[@class="btn-publication-detail"]/text()').get(),
                'price': element.xpath('//p[@class="prix"]/span/text()').get(),
                'seller type': element.xpath('//p[@class="type-vendeur type-vendeur-pro"]/text()').get(),
                'year': element.xpath('//ul[@class="list-info-detail clearfix"]/li[@class="no-pad-left"]/text()').get(),
                'kms': element.xpath('//ul[@class="list-info-detail clearfix"]/li/text()').get(), #fail
                'cylinders': element.xpath('//ul[@class="list-info-detail clearfix"]/li[@class="no-border"]/text()').get(),
                'colour': element.xpath('//ul[@class="list-info-detail clearfix"]/li[@class="no-pad-left"]/text()').get(), #fail
                'category': element.xpath('//ul[@class="list-info-detail clearfix"]/li[@class="no-border"]/text()').get(), #fail
                'description': element.xpath('//p[@class="descri-part"]/span/text()').get(),
                'localisation': element.xpath('//div[@class="content-map"]/text()').get(), #fail
                
                #'links': element.xpath('//a[@class="external btn-plus "]/@href').getall(),
            }

# Run spiders sequentially
configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
runner = CrawlerRunner()

@defer.inlineCallbacks
def crawl():
    yield runner.crawl(LPMTriumphDaytonaLinksSpider)
    #yield runner.crawl(LPMTriumphDaytonaSalesSpider)
    reactor.stop()

crawl()
reactor.run() # the script will block here until the last crawl call is finished


"""
Avoiding getting banned

Some websites implement certain measures to prevent bots from crawling them, with varying degrees of sophistication. Getting around those measures can be difficult and tricky, and may sometimes require special infrastructure. Please consider contacting commercial support if in doubt.

Here are some tips to keep in mind when dealing with these kinds of sites:

    rotate your user agent from a pool of well-known ones from browsers (google around to get a list of them)

    disable cookies (see COOKIES_ENABLED) as some sites may use cookies to spot bot behaviour

    use download delays (2 or higher). See DOWNLOAD_DELAY setting.

    if possible, use Google cache to fetch pages, instead of hitting the sites directly

    use a pool of rotating IPs. For example, the free Tor project or paid services like ProxyMesh. An open source alternative is scrapoxy, a super proxy that you can attach your own proxies to.

    use a highly distributed downloader that circumvents bans internally, so you can just focus on parsing clean pages. One example of such downloaders is Crawlera

"""

# scrapy shell 'http://localhost:8050/render.html?url=https://www.leparking-moto.fr/moto-occasion/triumph-daytona-675-france.html#!/moto-occasion/triumph-daytona-675.html%3Ftri%3Ddate&timeout=10&wait=0.5'

"""
idees
selenium
proxuy agent
"""
