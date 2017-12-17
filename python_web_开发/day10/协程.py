#_author_='shaojie'
#-*- coding:utf-8 -*-


from greenlet import greenlet

def test():
    print("hello")
    g2.switch()
    print("china")
    g2.switch()

def test1():
    print("你好")
    g1.switch()
    print('中国')

g1 = greenlet(test) # 建立g1协程
g2 = greenlet(test1) # 建立g2协程
g1.switch() # 首先切换到第一个协程执行操作
