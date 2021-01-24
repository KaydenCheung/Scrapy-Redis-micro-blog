import scrapy
from scrapy import Request
from weiboSpider.items import WeibospiderItem
import time

class WeibospiderSpider(scrapy.Spider):
    name = 'weibospider'
    start_urls = ['https://s.weibo.com/top/summary?cate=realtimehot']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
        # 'Cookie': '_T_WM=29225193880; BAIDU_SSP_lcr=https://www.google.com/; '
        #           'SUB=_2A25NDQEODeRhGeNH61UV8C3Izj6IHXVu8a9GrDV6PUJbktANLXWjkW1NSvegmyBX0oPqVdafKYiBnxRUArl4EwHK; '
        #           'SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5.q_dJWDLANz.-gZ9xXzds5NHD95Qf1K5NSh50Sh-EWs4Dqcj_i--Xi-zRi'
        #           '-zci--ci-zpiKLsi--fi-zNi-2ci--4iK.Ei-z7i--4iKn0iKy8; SSOLoginState=1611231582 '
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


