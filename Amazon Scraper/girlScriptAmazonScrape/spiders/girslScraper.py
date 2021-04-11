import json
import scrapy
from ..items import GirlscriptamazonscrapeItem

class girlScraper(scrapy.Spider):
        name = "girl"
        page_size=2
        start_urls = ["https://www.amazon.com/s?k=books&i=stripbooks&rh=n%3A283155%2Cp_n_publication_date%3A1250228011&dc&page=1&qid=1618076060&rnid=1250225011&ref=sr_pg_2"]
        def parse(self, response, **kwargs):
            items=GirlscriptamazonscrapeItem()
            name=response.css('.a-color-base.a-text-normal::text').extract()
            name=json.dumps(name)
            author=response.css('.a-spacing-top-small .a-color-secondary .a-size-base').css('::text').extract()
            price=response.css('.a-price-whole::text').extract()
            price=json.dumps(price)
            image_link=response.css('.s-image').get()
            image_link=json.dumps(image_link)

            items['name']=name
            items['author']=author
            items['price']=price
            items['image_link']=image_link

            yield items
            next_page = "https://www.amazon.com/s?k=books&i=stripbooks&rh=n%3A283155%2Cp_n_publication_date%3A1250228011&dc&page="+str(girlScraper.page_size)+"&qid=1618076060&rnid=1250225011&ref=sr_pg_2"
            if girlScraper.page_size <= 50:
                girlScraper.page_size += 1
                yield response.follow(next_page, callback=self.parse)
