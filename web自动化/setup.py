#_author_='shaojie'
#-*- coding:utf-8 -*-


import os

if __name__ == '__main__':
    installFile = os.path.join(os.getcwd(), 'lib.txt')
    os.system('pip install -r '+installFile)