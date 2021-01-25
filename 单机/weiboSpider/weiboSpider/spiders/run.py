import os
import time

if __name__ == '__main__':
    # os.system('pwd')
    while True:
        os.system("scrapy crawl weibospider -o title.csv")
        time.sleep(720)
