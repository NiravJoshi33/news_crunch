from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
import news_scrapper.spiders.news_spider1 as ns1
import news_scrapper.spiders.news_spider2 as ns2
import news_scrapper.spiders.news_spider4 as ns4
import news_scrapper.spiders.news_spider5 as ns5
import news_scrapper.spiders.news_spider6 as ns6


# def run_spiders():
#     settings = get_project_settings()
#     process = CrawlerProcess(settings)

#     spider_names = process.spider_loader.list()
#     for spider_name in spider_names:
#         print(f"Running Spider {spider_name}")
#         process.crawl(spider_name, query="dvh")

#     process.start()

# if __name__ == "__main__":
#     run_spiders()

ns1.configure_logging()
ns1.run_spider(ns1)

ns2.configure_logging()
ns2.run_spider(ns2)

ns4.configure_logging()
ns4.run_spider(ns4)

ns5.configure_logging()
ns5.run_spider(ns5)

ns6.configure_logging()
ns6.run_spider(ns6)