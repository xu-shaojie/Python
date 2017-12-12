#_author_='shaojie'
#-*- coding:utf-8 -*-

import os
from JSON import Json
from Python.FTP.ftp_client.DB import settings


class User(object):

    def __init__(self):
        self.json = Json()

    def login(self):
        user = input('请输入你的用户名')
        file = settings.base_dir + user + '.json'
        if os.path.isfile(file):
            password = input('请输入你的password')
            info = self.json.read(file)
            if info['password'] == password:
                print('login success')
                return user
            else:
                print('password is error')
        else:
            print('username input error ,re-input')

    def register(self):
        user = input('请输入你的用户名')
        file = settings.base_dir + user + '.json'
        if os.path.isfile(file):
            print('%s is exist,re-login')
        else:
            if user.isdigit():
                password = input('请输入你的密码')
                info ={
                    'user': user,
                    'password': password
                }
                self.json.write(file, info)
                return user
            else:
                pass