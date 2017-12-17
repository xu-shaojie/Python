#_author_='shaojie'
#-*- coding:utf-8 -*-

from gevent import monkey
import gevent
import socket

monkey.patch_all()

def server_socket(port):
    """
    首先,建立socket服务端,一直等待客户端请求。
    :param port:
    :return:
    """
    s = socket.socket()
    s.bind(("127.0.0.1",port))
    s.listen(10)
    while True:
        """ 等到客户端请求后,启动一个协程调用handle_request方法"""
        conn,addr = s.accept()
        gevent.spawn(handle_request,conn)

def handle_request(conn):
    try:
        while True:
            """ handle_request用于处理客户端的请求"""
            request = conn.recv(1024)
            conn.send(request.upper())
            if not request:
                conn.shoudown()
    except Exception as e:
        print(e)
    finally:
        conn.close()

if __name__ == "__main__":
    server_socket(5555)