# _author_='shaojie'
# -*- coding:utf-8 -*-

from Python.web自动化.page.login import Login
import unittest
import ddt


@ddt.ddt
class Test_Login(unittest.TestCase):

    def setUp(self):
        self.driver = Login()

    def tearDown(self):
        self.driver.close()

    @ddt.data(["1115041402@qq.com", "", "False"],
              ["", "password", "False"],
              ["", "", "False"],
              ["1115041402@qq.com", "shaojie9521", "True"])
    @ddt.unpack
    def test_01(self, user, pwd, ass):
        self.driver.open("http://www.lemfix.com/signin")
        self.driver.input_user(user)
        self.driver.input_password(pwd)
        self.driver.click_login_button()
        first = self.driver.alert()
        self.assertEqual(first, ass)

