import scrapy


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


from scrapy.crawler import CrawlerProcess

status = CrawlerProcess({
    'USER_AGENT' : 'Mozilla/5.0',
    'FEED_FORMAT' : 'csv',
    'FEED_URI' : 'coinedition.csv',
})

status.crawl(NewsSpider4Spider)
status.start()
status.stop()
    
