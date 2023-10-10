import scrapy


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

status = CrawlerProcess({
    'USER_AGENT' : 'Mozilla/5.0',
    'FEED_FORMAT' : 'csv',
    'FEED_URI' : 'dailyhold.csv',
})

status.crawl(NewsSpider1Spider)
status.start()
status.stop()