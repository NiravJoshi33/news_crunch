import scrapy


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

from scrapy.crawler import CrawlerProcess

status = CrawlerProcess({
    'USER_AGENT' : 'Mozilla/5.0',
    'FEED_FORMAT' : 'csv',
    'FEED_URI' : 'utoday.csv',
})

status.crawl(NewsSpider5Spider)
status.start()
status.stop()
