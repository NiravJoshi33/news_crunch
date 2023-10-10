import scrapy


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

status = CrawlerProcess({
    'USER_AGENT' : 'Mozilla/5.0',
    'FEED_FORMAT' : 'csv',
    'FEED_URI' : 'newsbtc.csv',
})

status.crawl(NewsSpider6Spider)
status.start()
status.stop()