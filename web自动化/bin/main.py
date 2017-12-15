#_author_='shaojie'
#-*- coding:utf-8 -*-

from Python.web自动化.bin.test_case_management import allTest
from Python.web自动化.common.HTMLTestRunner import HTMLTestRunner
import time
import os

if __name__ == "__main__":
    now = time.strftime('%Y-%m-%d %H-%m', time.localtime(time.time()))
    file = os.path.dirname(os.getcwd())
    new_file = file + "\\report" + now + ".html"
    fb = open(new_file, 'wb')
    suite = allTest()
    run1 = HTMLTestRunner(stream=fb, title="自动化测试报告",description="web自动化")
    run1.run(suite)
    fb.close()