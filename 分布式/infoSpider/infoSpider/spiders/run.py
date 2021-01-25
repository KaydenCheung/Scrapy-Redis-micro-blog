import os
import time
import redis

if __name__ == '__main__':
    # os.system('pwd')
    r = redis.Redis(host='47.102.204.46', port=6379, decode_responses=True)
    while True:
        os.system("scrapy runspider infospider.py")
        time.sleep(2)
                                                                                    
