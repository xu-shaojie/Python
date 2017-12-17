#_author_='shaojie'
#-*- coding:utf-8 -*-

from multiprocessing import Pipe,Process

def response(client):
    """
    response函数接收到客户端,便可以与服务端进行通信
    :param client:
    :return:
    """
    print(client.recv())
    client.send("蘑菇头收到")


if __name__ == "__main__":
    # 创建一个Pipe实例会返回管道的2边,类似socket,一端做服务端,一端做客户端
    server,client = Pipe()
    p = Process(target=response,args=(client,)) # 创建一个进程将client客户端传入response函数
    p.start() # 启动进程
    server.send('呼叫蘑菇头')
    print(server.recv())