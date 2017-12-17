#_author_='shaojie'
#-*- coding:utf-8 -*-

def get(name):
    print("%s开始吃包子了"%name)
    while True:
        baozi = yield
        print("%s eating baozi[%s]号"%(name,baozi))

def put():
    print("我要开始造包子了")

    g1 = get("胖")
    g2 = get("瘦")
    g1.__next__()
    g2.__next__()
    count = 0
    while count <5:
        count+=1
        print('现在制造的是包子',count)
        g1.send(count)
        g2.send(count)
    print('包子制作结束')

put()
