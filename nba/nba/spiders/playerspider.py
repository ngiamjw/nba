import scrapy


class PlayerspiderSpider(scrapy.Spider):
    name = "playerspider"
    allowed_domains = ["www.basketball-reference.com"]
    start_urls = ["https://www.basketball-reference.com/players/"]

    def parse(self, response):
        pass
