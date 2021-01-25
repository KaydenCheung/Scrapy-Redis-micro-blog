import scrapy
from scrapy import Request
from infoSpider.items import InfospiderItem


class InfospiderSpider(scrapy.Spider):
    name = 'infospider'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    }

    start_urls = []
    f = open('C:\\Users\\ybzhang\\Desktop\\url.txt', 'r')
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if line:
            start_urls.append(str(line))

    def start_requests(self):
        for i in range(len(self.start_urls)):
            yield Request(self.start_urls[i], headers=self.headers)

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
