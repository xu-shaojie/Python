# _author_='shaojie'
# -*- coding:utf-8 -*-

import socket
import os
import json
from author import User

class FTP(object):

    def __init__(self):
        self.client = socket.socket()
        self.user = User()

    def connect(self, host, port):
        self.client.connect((host, port))

    def login(self):
        user = self.user.login()
        info = {
            'user':user,
            'action':'login'
        }
        self.client.send(json.dumps(info).encode())
        response = self.client.recv(1024)
        print(response.decode())

    def register(self):
        user = self.user.register()
        info = {
            'user':user,
            'action':'register'
        }
        self.client.send(json.dumps(info).encode())
        response = self.client.recv(1024)
        print(response.decode())

    def help(self):
        menu = u'''
        login
        register
        ls
        cd
        pwd
        get filename
        push filename
        '''
        print(menu)

    def cd(self, *args):
        cmd_str = args[0]
        data = {'action': 'cd',
                'filename': cmd_str.split()[1]}
        self.client.send(json.dumps(data).encode())
        response = self.client.recv(1024).decode()
        print(response)

    def ls(self,args):
        cmd = args[0]
        # print(cmd)
        data = {
                    'action': 'ls'
                }
        self.client.send(json.dumps(data).encode())
        response = self.client.recv(1024)
        print(response)


    def pwd(self,*args):
        cmd = args[0]
        # print(cmd)
        data = {
            'action':'pwd'
        }
        self.client.send(json.dumps(data).encode())
        response = self.client.recv(1024)
        print(response)

    def put(self, *args):
        cmd_dic = args[0].split()
        print(cmd_dic)
        if len(cmd_dic) > 1:
            filename = cmd_dic[1]
            if os.path.isfile(filename):
                filesize = os.stat(filename).st_size
                data = {
                    'filename': filename,
                    'size': filesize,
                    'action': 'put'
                }
                self.client.send(json.dumps(data).encode())  # json序列化
                code = self.client.recv(1024)  # 防止粘包
                print(code)
                f = open(filename, 'rb')
                for line in f:
                    self.client.send(line)
                else:
                    print('文件发送完毕')
                    f.close()
            else:
                print('filename not exist')
        else:
            self.help()

    def get(self, *args):
        cmd_str = args[0]
        filename = cmd_str.split()[1]
        data = {
            'action': 'get',
            'filename': filename
        }
        self.client.send(json.dumps(data).encode())
        filesize = self.client.recv(1024).decode()
        self.client.send(b'200')  # ACK应答,防止粘包
        size = 0
        f = open(filename,'wb')
        while size < int(filesize):
            msg = self.client.send(1024)
            f.write(msg)
            size += len(msg)
        else:
            f.close()
            print('receive file success')

    def interaction(self):
        while True:
            cmd_str = input('>>:')
            if len(cmd_str) == 0:continue
            cmd = cmd_str.split()[0]
            print(cmd)
            if hasattr(self, cmd):
                fun = getattr(self, cmd)
                # print(fun)
                fun(cmd_str)
            else:
                print('input command error,re-enter')
                self.help()

f = FTP()
f.connect('localhost',9999)
chose = input('login or register')
if chose == 'login':
    f.login()
    f.interaction()
elif chose == 'register':
    f.register()
    f.login()
    f.interaction()

