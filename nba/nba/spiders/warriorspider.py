import scrapy
from nba.items import NbaItem


class WarriorspiderSpider(scrapy.Spider):
    name = "warriorspider"
    allowed_domains = ["https://www.basketball-reference.com/"]
    start_urls = ["https://www.basketball-reference.com/teams/GSW/2023_games.html"]

    def parse(self, response):
        pass