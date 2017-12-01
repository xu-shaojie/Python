# _author_='shaojie'
# -*- coding:utf-8 -*-

import socketserver
import json
import os


class Me_socket(socketserver.BaseRequestHandler):

    def setup(self):
        self.current_dir = os.path.dirname(os.getcwd()) + '/home'

    def cd(self,*args):
        cmd_dic = args[0]
        print(cmd_dic)
        file = cmd_dic['filename']
        if file == '..':
            self.current_dir = os.path.dirname(self.current_dir)
            self.request.send(self.current_dir.encode())
        elif os.path.isdir(self.current_dir + '/' + file):
            self.current_dir = self.current_dir + '/' + file
            print(self.current_dir)
            self.request.send(self.current_dir.encode())
        else:
            print('cmd input error,again input ')
            self.request.send(b'400,error')

    def pwd(self, *args):
        self.request.send(self.current_dir.encode())

    def ls(self,*args):
        file = os.listdir(self.current_dir)
        print(file)
        self.request.send(str(file).encode())

    def put(self, *args):
        cmd_dic = args[0]
        filename = cmd_dic['filename']
        filesize = cmd_dic['size']
        if os.path.isfile(filename):
            f = open(filename + 'new', 'wb')
        else:
            f = open(filename, 'wb')
        self.request.send(b'200,ok')
        size = 0
        while size < filesize:
            data = self.request.recv(1024)
            f.write(data)
            size += len(data)
            # print('已成功接收文件百分之%s'% int(filesize/size))
        else:
            f.close()
            print('receive file success')

    def get(self, *args):
        cmd_dic = args[0].split()
        # print(cmd_dic)
        if len(cmd_dic) > 1:
            filename = cmd_dic[1]
            file = self.current_dir + '/' + filename  # 拼接到HOME目录,只允许用户访问自己所在的目录
            if os.path.isfile(file):
                self.request.send(str(os.stat(file).st_size).encode())  # 发送文件大小
                self.request.recv(1024)  # ACK应答
                f = open(file, 'rb')
                for line in f:
                    self.request.send(line)
                else:
                    f.close()
                    print('send file success')
            else:
                self.request.send(b'403,error')

    def handle(self):
        """公共函数"""
        while True:
            try:
                self.msg = self.request.recv(1024)
                print('%s:%s execute %s'%(self.client_address[0],self.client_address[1],self.msg.decode()))
                cmd_dic = json.loads(self.msg.decode())
                action = cmd_dic['action']
                if hasattr(self, action):
                    fun = getattr(self, action)
                    fun(cmd_dic)
            except ConnectionResetError as e:
                print(e)
                break


if __name__ == "__main__":

    host, port = 'localhost',9999
    s = socketserver.ThreadingTCPServer((host,port),Me_socket)
    s.serve_forever()

