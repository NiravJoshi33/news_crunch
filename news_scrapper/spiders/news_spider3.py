import scrapy
import scrapy.crawler as crawler
from scrapy.utils.log import configure_logging
from multiprocessing import Process, Queue
from twisted.internet import reactor

class NewsSpider3Spider(scrapy.Spider):
    name = 'news_spider3'
    allowed_domains = ['theblock.co']
    start_urls = ['https://www.theblock.co/latest/']

    def parse(self, response):
        articles = response.css("article.articleCard.collectionLatest")

        for article in articles:

            article_relative_url = article.css("div.headline a::attr(href)").get()
            article_url = "https://www.theblock.co/latest" + article_relative_url
            # print("******")
            # print(article_url)
            yield response.follow(article_url, callback = self.parse_article_page)

    def parse_article_page(self, response):

            yield{
                "title": response.css("article.articleBody h1::text").get(),
                "author": response.css(".articleByline > label:nth-child(1) > a:nth-child(1)::text").get(),
                "date": response.css("div.timestamp.tbcoTimestamp::text").get(),
                "thumb": response.css(".articleFeatureImage img::attr(src)").get(),
                "excerpt": response.css("div.articleContent span p").get(),
                "article_url": response.css("head link[rel=canonical]::attr(href)").get(),
                "website_name": "The Block",
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
    'FEED_URI' : 'theblock.csv',
})

status.crawl(NewsSpider3Spider)
status.start()
status.stop()