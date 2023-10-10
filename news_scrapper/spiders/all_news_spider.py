import scrapy
import scrapy.crawler as crawler
from scrapy.utils.log import configure_logging
from multiprocessing import Process, Queue
from twisted.internet import reactor

class NewsSpider1Spider(scrapy.Spider):
    name = 'all_news_spider'
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

class NewsSpider4Spider(scrapy.Spider):
    name = 'news_spider4'
    allowed_domains = ['coinedition.com']
    start_urls = ['http://coinedition.com/news/']

    def parse(self, response):
        articles = response.css(".ce-catag-leftblock-container .ce-catag-leftblock-each")
        
        for article in articles:
            article_url = article.css("div.ce-post-info h3 a::attr(href)").get()
            # print(f"\n\n\n {article_url}\n\n")
            if article_url:
                yield response.follow(article_url, callback = self.parse_article_page)

    def parse_article_page(self, response):

        yield{
            "title": response.css(".ce-single-post-title-block h1::text").get(),
            "author": response.css("div.ce-single-post-author span a::text").get(),
            "date": response.css("div.ce-single-post-updated span time::text").get(),
            "thumb": response.css("div.ce-single-post-featured-img-block img::attr(data-lazy-src)").get(),
            "excerpt": response.css("div.ce-single-post-content-block p").get(),
            "article_url": response.css("head link[rel=alternate]::attr(href)").get(),
            "website_name": "Coin Edition"
        }

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
            "author": response.css("a.article__lead-name::text").get(),
            "date": response.css("div.time::text").get(),
            "thumb": response.css("img.article__main-img::attr(src)").get(),
            "excerpt": response.css("div.article__content p").get(),
            "article_url": "http://u.today/" + response.css("div.article h1::attr(data-url)").get(),   
            "website_name": "U Today",
        }

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
    'FEED_URI' : 'thedailyhold.csv',
})

status.crawl(NewsSpider1Spider)

status = CrawlerProcess({
    'USER_AGENT' : 'Mozilla/5.0',
    'FEED_FORMAT' : 'csv',
    'FEED_URI' : 'finbold.csv',
})
status.crawl(NewsSpider2Spider)

status = CrawlerProcess({
    'USER_AGENT' : 'Mozilla/5.0',
    'FEED_FORMAT' : 'csv',
    'FEED_URI' : 'coinedition.csv',
})
status.crawl(NewsSpider4Spider)

status = CrawlerProcess({
    'USER_AGENT' : 'Mozilla/5.0',
    'FEED_FORMAT' : 'csv',
    'FEED_URI' : 'utoday.csv',
})
status.crawl(NewsSpider5Spider)

status = CrawlerProcess({
    'USER_AGENT' : 'Mozilla/5.0',
    'FEED_FORMAT' : 'csv',
    'FEED_URI' : 'newsbtc.csv',
})
status.crawl(NewsSpider6Spider)

status.start()
status.stop()