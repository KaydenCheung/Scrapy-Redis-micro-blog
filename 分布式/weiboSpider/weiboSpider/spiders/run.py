import os
import time
import redis

if __name__ == '__main__':
    # os.system('pwd')
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    while True:
        r.flushall()
        os.system("scrapy crawl weibospider")
        f = open('url.txt', 'r', encoding='utf-8')
        lines = f.readlines()
        for line in lines:
            r.lpush('weibo:start_urls', line)
        time.sleep(600)
