import scrapy
import scrapy.crawler as crawler
from scrapy.utils.log import configure_logging
from multiprocessing import Process, Queue
from twisted.internet import reactor

class NewsSpider1Spider(scrapy.Spider):
    name = 'news_spider1'
    allowed_domains = ['dailyhodl.com/']
    start_urls = ['https://dailyhodl.com/']

    def parse(self, response):
        articles = response.css("article.jeg_post.jeg_pl_lg_2.format-standard")

        for article in articles:
            yield{
                "title" : article.css("h3 a::text").get(),
                "author" : article.css("div.jeg_meta_author a::text").get(),
                "date" : article.css("div.jeg_meta_date a::text").get().strip(),
                "thumb" : article.css("img.attachment-jnews-350x250.size-jnews-350x250.wp-post-image ").attrib["src"],
                "excerpt" : article.css("div.jeg_post_excerpt p::text").get(),
                "article_url" : article.css("h3.jeg_post_title a::attr(href)").get(),
                "website_name" : "The Daily Hodl"
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
    'FEED_URI' : 'thedailyhold.csv',
})

status.crawl(NewsSpider1Spider)
status.crawl()
status.start()