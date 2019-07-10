import scrapy
from ..items import CountryItem
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup


class CitiesSpider(scrapy.Spider):
    name = "zomato"

    start_urls= ['https://www.zomato.com/directory']

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html5lib')
        for item in soup.select(".row h2 > a"):
            yield {"name":item.text}
            #yield city
         #item = {}
        #for city in response.css('.normal a'):
        #cities_name = response.xpath('//div//h2//a/text()').extract_first()
        #items['cities_name'] = cities_name
        #yield items
        #city = response.xpath("//div[@class='col-l-5 col-s-8 item pt0 pb5 ml0']//h2 [@class]").extract_first()
        #yield scrapy.Request(url = start_url, callback=self.parse)
        #cities_name = response.css('.normal a::text').extract()
        #items['cities_name'] = cities_name
        #yield items
        #soup = BeautifulSoup(response.text, 'html5lib')
       # for item in soup.select(".row h2 > a"):
            #yield {"cities_name":item.text}
