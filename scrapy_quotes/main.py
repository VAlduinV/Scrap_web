from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from Scrap_web.scrapy_quotes.scrapy_quotess.spiders.quotes_spider import QuotesSpider
from Scrap_web.scrapy_quotes.scrapy_quotess.spiders.authors_spider import AuthorsSpider


def main():
    quo_process = CrawlerProcess(get_project_settings())
    auth_process = CrawlerProcess(get_project_settings())
    quo_process.crawl(QuotesSpider)
    quo_process.start()
    auth_process.crawl(AuthorsSpider)
    auth_process.start()


if __name__ == "__main__":
    main()
