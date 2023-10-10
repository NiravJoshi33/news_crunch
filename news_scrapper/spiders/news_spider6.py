import scrapy
import scrapy.crawler as crawler
from scrapy.utils.log import configure_logging
from multiprocessing import Process, Queue
from twisted.internet import reactor

class NewsSpider6Spider(scrapy.Spider):
    name = 'news_spider6'
    allowed_domains = ['newsbtc.com']
    start_urls = ['https://www.newsbtc.com/news//']

    def parse(self, response):
        articles = response.css("article.jeg_post.jeg_pl_md_2.format-standard")

        for article in articles:
            yield{
                "title": article.css("h3.jeg_post_title a::text").get(),
                "author": article.css("div.jeg_meta_author a::text").get(),
                "date": article.css("div.jeg_meta_date a::text").get(),
                "thumb": article.css("img.attachment-jnews-350x250::attr(data-src)").get(),
                "excerpt": article.css("div.jeg_post_excerpt p::text").get(),
                "article_url": article.css("div.jeg_thumb a::attr(href)").get(),
                "website_name": "NEWSBTC"
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
    'FEED_URI' : 'newsbtc.csv',
})

status.crawl(NewsSpider6Spider)
status.start()
status.stop()