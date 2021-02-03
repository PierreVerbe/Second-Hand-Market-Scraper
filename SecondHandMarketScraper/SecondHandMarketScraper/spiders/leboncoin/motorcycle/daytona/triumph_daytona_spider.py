import scrapy
import logging
from selenium import webdriver

class TriumphDaytonaSpider(scrapy.Spider):
    name = 'Triumph_Daytona_Spider'

    """
    start_urls = [
            'https://www.leboncoin.fr/recherche?category=3"&"moto_brand=triumph"&"moto_model=Daytona"&"regdate=2005-max',
        ]
    """

    start_urls = [
        'http://www.ebay.com/sch/i.html?_odkw=books&_osacat=0&_trksid=p2045573.m570.l1313.TR0.TRC0.Xpython&_nkw=python&_sacat=0&_from=R40',
    ]

    def __init__(self):
        self.driver = webdriver.Firefox()
    

    """
    # & is not authorized so use insted "&"
    def start_requests(self):
        urls = [
            'https://www.leboncoin.fr/recherche?category=3"&"moto_brand=triumph"&"moto_model=Daytona"&"regdate=2005-max',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    """

    def parse(self, response):
        self.driver.get(response.url)

        while True:
            print("hello")
            next = self.driver.find_element_by_xpath('//td[@class="pagn-next"]/a')

            try:
                next.click()

                # get the data and write it to scrapy items
            except:
                break

        self.driver.close()

        """
        for element in response.css(''):
            yield {
                'title': quote.xpath('/html/body/div[2]/div/section/main/div/div[1]/div[6]/div/div[5]/div[1]/div[1]/div[7]/a/div/div/div/div[1]/div[2]/div[1]/div[1]/div[1]/p').get(),
                'price': quote.xpath('/html/body/div[2]/div/section/main/div/div[1]/div[6]/div/div[5]/div[1]/div[1]/div[7]/a/div/div/div/div[1]/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/span/span').get(),
            }

        # Write into a file
        filename = f'quotes.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
        """

            