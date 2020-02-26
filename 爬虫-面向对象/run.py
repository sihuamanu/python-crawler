import threading
import time
import datetime

from config import Page_URL
from config import ANALYSER
from spider import Spider

def go():
    spider = Spider(Page_URL, ANALYSER)
    spider.go()
    print(str(datetime.datetime.now()) + '--------------------')
    time.sleep(600)
    timer = threading.Timer(0, go)
    timer.start()

timer = threading.Timer(0, go)
timer.start()