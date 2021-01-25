import scrapy
from scrapy import Request
from infoSpider.items import InfospiderItem


class InfospiderSpider(scrapy.Spider):
    name = 'infospider'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
        # 'Cookie': '_T_WM=29225193880; BAIDU_SSP_lcr=https://www.google.com/; '
        #           'SUB=_2A25NDQEODeRhGeNH61UV8C3Izj6IHXVu8a9GrDV6PUJbktANLXWjkW1NSvegmyBX0oPqVdafKYiBnxRUArl4EwHK; '
        #           'SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5.q_dJWDLANz.-gZ9xXzds5NHD95Qf1K5NSh50Sh-EWs4Dqcj_i--Xi-zRi'
        #           '-zci--ci-zpiKLsi--fi-zNi-2ci--4iK.Ei-z7i--4iKn0iKy8; SSOLoginState=1611231582 '
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
        # infos = div.xpath('//p[@class="txt" and @node-type="feed_list_content"]')

        for info in infos:
            item = InfospiderItem()
            # item['content'] = info.xpath(
            #     './/p[@class="txt" and @node-type="feed_list_content"]').xpath('string(.)').extract()[0].strip()
            text = info.xpath('.//p[@class="txt" and @node-type="feed_list_content"]')
            if text:
                item['content'] = text.xpath(
                    'string(.)').extract()[0].strip().replace('\n', '')
                item['title'] = response.xpath('//input[@type="text" and @node-type="text" and @maxlength="40" and '
                                               '@autocomplete="off"]/@value').extract()[0].strip()
                yield item
