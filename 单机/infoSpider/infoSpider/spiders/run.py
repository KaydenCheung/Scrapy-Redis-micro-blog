import os
import time

if __name__ == '__main__':
    # os.system('pwd')
    while True:
        os.system("scrapy crawl infospider -o info.csv")
        time.sleep(1)