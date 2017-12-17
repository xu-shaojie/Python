#_author_='shaojie'
#-*- coding:utf-8 -*-

import unittest
import gevent


class Test(unittest.TestCase):

    def test1(self):
        print("in the test1")
        gevent.sleep(1)
        print("test stop...")


    def test2(self):
        print("in the test2")

gevent.joinall(
    [gevent.spawn(Test)]
)