import scrapy
class QuotesSpider(scrapy.Spider):
    name='codesss'

    def start_requests(self):
        urls=['http://quotes.toscrape.com/page/1/'
            ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self,response):

        page= response.url.split("/")[-2]
        filename= "quotes%s.html"%page


        for quote in response.css('div.quote'):
            text= quote.css('span.text::text').get()
            author= quote.css('small.author::text').get()
            tags= quote.css('a.tag::text').getall()
            yield{
            'text':text,
            'author':author,
            'tags':tags
            }
       # with open(filename,'wb') as f:
        #    f.write(response.body)
       # self.log('saved file %s' %filename)
