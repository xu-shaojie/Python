#_author_='shaojie'
#-*- coding:utf-8 -*-

import gevent

# 遇见IO就切换
def eat():
    print("eating apple")
    gevent.sleep(1)
    print("eating ice")

def write():
    print("write code")
    gevent.sleep(2)
    print('write book')

gevent.joinall(
    [gevent.spawn(eat),
     gevent.spawn(write)]
)
