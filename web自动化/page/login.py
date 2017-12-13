# _author_='shaojie'
# -*- coding:utf-8 -*-

from web.common.web_selenium import MyTest
import time


class Login(MyTest):

    def input_user(self, user):
        """
        输入用户名
        :param user:
        :return:
        """
        self.send_keys("id->name", user)

    def input_password(self, pwd):
        """
        输入密码
        :param pwd:
        :return:
        """
        self.send_keys("id->pass", pwd)

    def click_login_button(self):
        """
        点击登录按钮
        :return:
        """
        self.click("css->#signin_form > div.form-actions > input")

    def click_forget_password(self):
        """
        点击忘记密码
        :return:
        """
        self.click("id->forgot_password")

    def alert(self):
        if self.find_element("css->#content > div > div.inner > div > strong"):
            return False
        else:
            return True
