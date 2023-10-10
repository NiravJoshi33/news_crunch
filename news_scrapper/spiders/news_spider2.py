import scrapy
import scrapy.crawler as crawler
from scrapy.utils.log import configure_logging
from multiprocessing import Process, Queue
from twisted.internet import reactor

class NewsSpider2Spider(scrapy.Spider):
    name = 'news_spider2'
    allowed_domains = ['finbold.com']
    start_urls = ['https://finbold.com/category/cryptocurrency-news/']

    def parse(self, response):
        articles = response.css("div.flex.gap-x-4")
        relative_url = response.css("a.relative[aria-label='pagination.next']::attr(href)").get()
        print(f"relative url: {relative_url}")

        for article in articles:

            article_url = article.css("h3 a").attrib["href"]
            yield response.follow(article_url, callback = self.parse_article_page)

        if relative_url is not None:
            next_page = "https://finbold.com" + relative_url
            print(f"\n\n{next_page}\n\n")
        yield response.follow(next_page, callback = self.parse)


    def parse_article_page(self, response):
        print("this function is entered")

        yield{
            "title" : response.css("h1.entry-title::text").get(),
            "author" : response.css("a.mb-1.block span.self-center.text-sm.text-slate-500.author.vcard.byline::text").get(),
            "date" : response.css("time.updated::text").get(),
            "thumb" : response.css("img.attachment-large::attr(src)").get(),
            "excerpt" : response.css("p.paragraph").get(),
            "article_url" : response.css("head link[rel=canonical]::attr(href)").get(),
            "website_name" : "Finbold"
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
    'FEED_URI' : 'finbold.csv',
})

status.crawl(NewsSpider2Spider)
status.start()
status.stop()