import scrapy
from scrapy import Request
from infoSpider.items import InfospiderItem
from scrapy_redis.spiders import RedisSpider


class InfospiderSpider(RedisSpider):
    name = 'infospider'
    # headers = {
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    # }


    redis_key = 'weibo:start_urls'


    def parse(self, response):
        infos = response.xpath('//div[@class="card-wrap" and not(div[@class="card-top"])]')

        for info in infos:
            item = InfospiderItem()
            text = info.xpath('.//p[@class="txt" and @node-type="feed_list_content"]')
            if text:
                item['content'] = text.xpath(
                    'string(.)').extract()[0].strip().replace('\n', '')
                item['title'] = response.xpath('//input[@type="text" and @node-type="text" and @maxlength="40" and '
                                               '@autocomplete="off"]/@value').extract()[0].strip()
                yield item
