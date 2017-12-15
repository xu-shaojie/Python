# _author_='shaojie'
# -*- coding:utf-8 -*-

from Python.web自动化.test_case.test_login import Test_Login
from Python.web自动化.common.HTMLTestRunner import HTMLTestRunner
from unittest import TestLoader,TestSuite,TestCase
import time
import os


# 用例管理模块
case_list = {
    "Test_Login": Test_Login
}


def allTest():
    f = open('test_case_management.txt','r',encoding='utf-8')
    cases = []
    for i in f:
        if i.strip() in case_list and "#" not in i.strip():
            case = TestLoader().loadTestsFromTestCase(case_list[i.strip()])
            cases.append(case)
        else:
            continue
    f.close()
    all_tests = TestSuite(cases)
    return all_tests
