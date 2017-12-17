#_author_='shaojie'
#-*- coding:utf-8 -*-

from multiprocessing import Process,Manager
import os


"""
manager为什么能实现进程之间的数据共享呢？
那是因为manager跟进程的Queue(队列)一样。将数据克隆给每一个进程,并放在中间地址，
每个进程操作之后，将数据返回给中间地址,manager再通过序列化将数据读取回来。这样就实现了进程之间数据的共享
"""

# 定义一个r函数。用来进行进程之间数据的共享操作
def r(d,l):
    d[os.getpid()] = os.getpid()
    l.append(os.getpid())
    print(l)

if __name__ == "__main__":
    manager = Manager()
    dic = manager.dict() # 定义一个可以进程之间共享数据的字典
    lis = manager.list()

    process_list = []
    for i in range(5):
        p = Process(target=r,args=(dic,lis))
        process_list.append(p)
        p.start()

    for i in process_list:
        i.join()

    print(dic)
    print(lis)