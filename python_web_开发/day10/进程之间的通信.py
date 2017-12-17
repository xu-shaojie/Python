#_author_='shaojie'
#-*- coding:utf-8 -*-

from multiprocessing import Process,Queue
import threading

"""
def info(que):
    que.put(1)

if __name__ == "__main__":
    q = Queue()
    t = threading.Thread(target=info,args=(q,))
    t.start()
    print(q.get())"""

from multiprocessing import Process,Queue
import queue

def info(que):
    que.put(1)

if __name__ == "__main__":
    q = Queue() # 创建一个进程队列
    t = Process(target=info,args=(q,)) #创建一个进程实例
    t.start()
    print(q.get())

