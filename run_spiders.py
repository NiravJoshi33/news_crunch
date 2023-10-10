from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess

def run_spiders():
    settings = get_project_settings()
    process = CrawlerProcess(settings)

    spider_names = process.spider_loader.list()
    for spider_name in spider_names:
        print(f"Running Spider {spider_name}")
        process.crawl(spider_name, query="dvh")

    process.start()

if __name__ == "__main__":
    run_spiders()