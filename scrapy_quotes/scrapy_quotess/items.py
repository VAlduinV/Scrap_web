import scrapy


class QuoteItem(scrapy.Item):
    quote = scrapy.Field()
    author = scrapy.Field()


class AuthorItem(scrapy.Item):
    name = scrapy.Field()
    quotes = scrapy.Field()
