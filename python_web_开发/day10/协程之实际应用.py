#_author_='shaojie'
#-*- coding:utf-8 -*-

import gevent,time
from urllib.request import urlopen
import unittest
from gevent import monkey

# monkey.patch_all()相当于给每个IO操作都打上了一个标记.后续,gevent运行时遇见IO就进行切换
monkey.patch_all()


def open(url):
    response = urlopen(url)
    data = response.read()
    print("%s byte received from %s"%(len(data),url))

start_time = time.time()
url_list = ["http://www.python.org","http://www.jianshu.com","http://www.github.com"]
for url in url_list:
    open(url)
print("同步cost的时间:",time.time()-start_time)

async_time_start = time.time()
gevent.joinall(
    [gevent.spawn(open,"http://www.python.org"),
     gevent.spawn(open,"http://www.jianshu.com"),
     gevent.spawn(open,"http://www.github.com")])
print("异步cost的时间:",time.time()-async_time_start)
