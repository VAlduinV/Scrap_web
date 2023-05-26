import scrapy
from Scrap_web.scrapy_quotes.scrapy_quotess.items import AuthorItem


class AuthorsSpider(scrapy.Spider):
    name = "authors"
    start_urls = ["http://quotes.toscrape.com"]

    def parse(self, response):
        for quote in response.css("div.quote"):
            item = AuthorItem()
            item["name"] = quote.css("span small::text").get()
            item["quotes"] = [quote.css("span.text::text").get()]
            yield item
        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
