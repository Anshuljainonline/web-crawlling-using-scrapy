import scrapy

class BookSpider(scrapy.Spider):
    name='Bookspider'

    def start_requests(self):

        url='http://books.toscrape.com/'
        yield scrapy.Request(url=url, callback= self.parse)

    def parse(self, response):

        for book in response.css('article.product_pod'):
            image_url = book.css('div.image_container img::attr(src)').get()
            name = book.css('div.image_container img::attr(alt)').get()
            price = book.css('div.product_price p.price_color::text').get()

            yield{
                 'image url':image_url,
                 'book_title':name,
                 'product_price': price

                 }

        next_page= response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page= response.urljoin(next_page)
            yield scrapy.Request(next_page,callback=self.parse)
