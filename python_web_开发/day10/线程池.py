#_author_='shaojie'
#-*- coding:utf-8 -*-

import time,os
from multiprocessing import Pool,Process


def info(num):
    time.sleep(2)
    print("hello,world")
    return num+1

def pid(arg):
    print("线程:",arg,os.getpid())

if __name__ == "__main__":
    # pool相当于一个池子。这里同时启动了5个线程,但是没有进行操作
    pool = Pool(5)
    for i in range(10):
        """ 线程池异步(pool_apply_async())执行，并进行函数回调
        线程池同步执行,相当于串行 pool.apply(func,callback=None,*args,*kwds)
        """
        pool.apply_async(func=info,args=(i,),callback=pid)
    print("end")
    pool.close()
    pool.join()