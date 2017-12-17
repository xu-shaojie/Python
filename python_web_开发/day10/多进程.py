#_author_='shaojie'
#-*- coding:utf-8 -*-

import multiprocessing,time,threading


def info():
    # 打印进程号
    print(threading.get_ident())


def f():
    print("hello,world")
    """ 启动一个线程 """
    t =threading.Thread(target=info)
    t.start()


if __name__ == "__main__":
    for i in range(5):
        """ 启动5个进程 """
        p = multiprocessing.Process(target=f)
        p.start()