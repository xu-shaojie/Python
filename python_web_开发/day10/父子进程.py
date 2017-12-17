#_author_='shaojie'
#-*- coding:utf-8 -*-

import threading,multiprocessing,time,os

"""
所有的子进程都是由主进程启动的
"""
def info(process):
    print(process)
    print("module name:",__name__)
    print("parent process:",os.getppid())
    print("process id:",os.getpid())
    time.sleep(1)

def run(name):
    t = threading.Thread(target=info,args=("run  process",))
    t.start()
    print("hello",name)

if __name__ == "__main__":
    info("main parent process ")
    p = multiprocessing.Process(target=run,args=('shaojie',))
    p.start()