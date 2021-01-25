import os
import time
import redis

if __name__ == '__main__':
    # os.system('pwd')
    r = redis.Redis(host='46.100.201.42', port=6379, decode_responses=True)
    while True:
        os.system("scrapy runspider infospider.py")
        time.sleep(2)
                                                                                    
