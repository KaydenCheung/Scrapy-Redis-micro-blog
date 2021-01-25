import scrapy
from scrapy import Request
from weiboSpider.items import WeibospiderItem
import time

class WeibospiderSpider(scrapy.Spider):
    name = 'weibospider'
    start_urls = ['https://s.weibo.com/top/summary?cate=realtimehot']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    }

    def start_requests(self):
        yield Request(self.start_urls[0], headers=self.headers)

    def parse(self, response):
        f = open('C:\\Users\\ybzhang\\Desktop\\url.txt', 'w+', encoding='utf-8')
        now_time = time.strftime("%Y-%m-%d %H:%M", time.localtime())
        titles = response.xpath('//tr[position()>1]')
        for title in titles:
            item = WeibospiderItem()
            item['rank'] = title.xpath(
                './/td[@class="td-01 ranktop"]/text()').extract()[0].strip()
            item['title'] = title.xpath(
                './/td[@class="td-02"]/a/text()').extract()[0].strip()
            item['degree'] = title.xpath(
                './/td[@class="td-02"]/span/text()').extract()[0].strip()
            item['time'] = now_time

            url = 'https://s.weibo.com/' + title.xpath(
                './/td[@class="td-02"]/a/@href').extract()[0].strip()
            f.write(url)
            f.write('\n')
            yield item


