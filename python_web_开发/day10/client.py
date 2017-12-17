#_author_='shaojie'
#-*- coding:utf-8 -*-

import socket



def client_socket(host,port):
    try:
        client = socket.socket()
        client.connect((host,port))
        while True:
            msg = input("<<:")
            client.sendall(msg.encode())
            response = client.recv(1024)
            print(response)
    except Exception as e:
        print(e)
    finally:
        client.close()

if __name__ =="__main__":
    host,port = "127.0.0.1",5555
    client_socket(host,port)