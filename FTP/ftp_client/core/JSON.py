# _author_='shaojie'
# -*- coding:utf-8 -*-

import json


class Json(object):
    """
    /* read 负责读取json文件
    write 负责写入json文件
    */
    """
    def read(self,filename):
        with open(filename,'r') as f:
            data = json.load(f)
            return data

    def write(self, filename, data):
        with open(filename, 'w') as f:
            json.dump(data, f)
