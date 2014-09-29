import scrapy
from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.bgcpasadena.org/news-events/"
        #"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        #"http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    #SOS
    #NOTES: http://doc.scrapy.org/en/latest/intro/tutorial.html
    #To run: scrapy crawl dmoz
    def parse(self, response):
        #filename = response.url.split("/")[-2]
        #with open(filename, 'wb') as f:
        #    f.write(response.body)

        for sel in response.xpath('//ul/li'):
            item = DmozItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            #yield item
            #print 123
            #print item['title']

        print ''
        print '*** START ***'
        #print response.xpath('//ul/li/a/@href').extract()
        #print response.xpath('//article/header/h1/a/@href').extract()
        for sel in response.xpath('//ul/li'):
            print sel.xpath('a/text()').extract()
            #print sel.xpath('//ul/li/span/text()').extract()
            print sel.xpath('span/text()').extract()
        print '*** END ***'
        print ''