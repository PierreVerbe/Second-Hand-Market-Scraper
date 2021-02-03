# Second-Hand-Market-Scraper

## About this repository

## Prerequisite
* Install Python 3 <br>
* Install an IDE <br>
* Install docker <br>

## Installation
* First clone this project
```bash
git clone https://github.com/PierreVerbe/Scala-Spark-Template
```

* Retrieve the docker container scrapinghub/splash
```bash
docker pull scrapinghub/splash
```

* Run the container scrapinghub/splash in localhost:8050
```bash
docker run -p 8050:8050 scraping/splash
```

* Install this python packages
```bash
pip install scrapy scrapy-splash
```

## Scrape a website
* Run a python file

* Use scrapy command
```bash
scrapy runspider SecondHandMarketScraper/SecondHandMarketScraper/spiders/folder/myFile.py
```

* Use scrapy shell with Splash
```bash
scrapy shell 'http://localhost:8050/render.html?url=https://www.website.fr&timeout=10&wait=0.5'
```

## Notes
* Can access the Splash rendering service
[Click here](http://localhost:8050)

## TODO List
- Finish markdown
- Next page
- Multiple URLs
- Write into file
- spider input is spider output


scrapy shell 'http://localhost:8050/render.html?url=https://www.leboncoin.fr/recherche?category=3"&"moto_brand=triumph"&"moto_model=Daytona"&"regdate=2005-max&timeout=10&wait=0.5'


b"styles_adListItem__3Z_IE styles_order2__2Kb_N" in response.body

response.body

response.xpath('//div[@class="styles_adListItem__3Z_IE styles_order2__2Kb_N"]')




proxy
pip install scrapy-proxy-pool

selenium
pip install selenium


ROBOTSTXT_OBEY = False

