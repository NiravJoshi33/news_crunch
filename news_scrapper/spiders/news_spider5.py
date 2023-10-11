import scrapy
import scrapy.crawler as crawler
from scrapy.utils.log import configure_logging
from multiprocessing import Process, Queue
from twisted.internet import reactor

class NewsSpider5Spider(scrapy.Spider):
    name = 'news_spider5'
    allowed_domains = ['u.today']
    start_urls = ['http://u.today/latest-cryptocurrency-news/']

    def parse(self, response):
        articles = response.css("div.category-item")

        for article in articles:
            article_url = article.css("div.category-item a.category-item__img-wrapper::attr(href)").get()
            
            if article_url:
                yield response.follow(article_url, callback = self.parse_article_page)

    def parse_article_page(self, response):

        yield{
            "title": response.css("div.article h1::text").get(),
            "author": response.css("div.article__author-name::text").get(),
            "date": response.xpath("/html/body/div[3]/div/main/div/div[1]/div/div[4]/div[1]/div/div[2]/text()").get(),
            "thumb": response.css("img.article__main-img::attr(src)").get(),
            "excerpt": response.css("div.article__content p").get(),
            "article_url": "http://u.today/" + response.css("div.article h1::attr(data-url)").get(),   
            "website_name": "U Today",
        }

from scrapy.crawler import CrawlerProcess

def run_spider(spider):
    def f(q):
        try:
            runner = crawler.CrawlerRunner()
            deferred = runner.crawl(spider)
            deferred.addBoth(lambda _: reactor.stop())
            reactor.run()
            q.put(None)
        except Exception as e:
            q.put(e)

    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    result = q.get()
    p.join()

    # if result is not None:
    #     raise result

status = CrawlerProcess({
    'USER_AGENT' : 'Mozilla/5.0',
    'FEED_FORMAT' : 'csv',
    'FEED_URI' : 'utoday.csv',
})

status.crawl(NewsSpider5Spider)
status.start()
status.stop()
