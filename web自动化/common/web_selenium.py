# _author_='shaojie'
# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class MyTest(object):

    def __init__(self):
        """
        这里稍微封装一下,就可以兼容其他浏览器
        :return:
        """
        self.driver = webdriver.Chrome()

    def find_element(self,css):
        """
        /* 通过以下方法寻找元素
        id: Finds an element by id.
        name: Finds an element by name.
        css_selector: Finds an element by css_selector
        xpath:  Finds an element by xpath.
        tag_name: Finds an element by tag_name.
        link_text: Finds an element by link_text.
        */
        Usage: self.find_element(css)
        :param css: id->kw
        :return:
        """
        key = css.split('->')[0]
        value = css.split('->')[1]

        if key == "id":
            ele = self.driver.find_element_by_id(value)
        elif key == "css":
            ele = self.driver.find_element_by_css_selector(value)
        elif key == "name":
            ele = self.driver.find_element_by_name(value)
        elif key == "xpath":
            ele = self.driver.find_element_by_xpath(value)
        elif key == "link":
            ele = self.driver.find_element_by_link_text(value)
        elif key == "tag":
            ele = self.driver.find_element_by_tag_name(value)
        else:
            raise NameError("输入参数错误...请检查")
        return ele

    def find_elements(self,css):
        """
        /* 通过以下方法寻找元素
        id: Finds multiple elements by id.
        name: Finds multiple element by name.
        css_selector: Finds multiple element by css_selector
        xpath:  Finds multiple element by xpath.
        tag_name: Finds multiple element by tag_name.
        link_text: Finds multiple element by link_text.
        */
        Usage: self.find_elements(css)
        :param css: id->kw
        :return:
        """
        key = css.split('->')[0]
        value = css.split('->')[1]

        if key == "id":
            ele = self.driver.find_elements_by_id(value)
        elif key == "css":
            ele = self.driver.find_elements_by_css_selector(value)
        elif key == "name":
            ele = self.driver.find_elements_by_name(value)
        elif key == "xpath":
            ele = self.driver.find_elements_by_xpath(value)
        elif key == "link":
            ele = self.driver.find_elements_by_link_text(value)
        elif key == "tag":
            ele = self.driver.find_elements_by_tag_name(value)
        else:
            raise NameError("输入参数错误...请检查")
        return ele

    def element_wait(self, css, timeout):
        key = css.split('->')[0]
        value = css.split('->')[1]
        message = ("Not find element:{1},Spend {2} seconds".format(css, timeout))
        if key == "id":
            WebDriverWait(self.driver,timeout, 0.5).until(EC.presence_of_element_located((By.ID, value)), message)
        elif key == "name":
            WebDriverWait(self.driver,timeout, 0.5).until(EC.presence_of_element_located((By.NAME, value)), message)
        elif key == "xpath":
            WebDriverWait(self.driver,timeout, 0.5).until(EC.presence_of_element_located((By.XPATH, value)), message)
        elif key == "css":
            WebDriverWait(self.driver,timeout, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)), message)
        elif key == "tag":
            WebDriverWait(self.driver,timeout, 0.5).until(EC.presence_of_element_located((By.TAG_NAME, value)), message)
        elif key == "link":
            WebDriverWait(self.driver,timeout, 0.5).until(EC.presence_of_element_located((By.LINK_TEXT, value)), message)
        else:
             raise NameError("Please enter the correct targeting elements,id,name,css_selector,link_text,xpath,css")

    def click(self, css):
        """
        点击
        :param css:
        :return:
        """
        try:
            self.element_wait(css, 10)
            ele = self.find_element(css)
            ele.click()
        except Exception as msg:
            raise msg

    def send_keys(self, css, text):
        """
        发送内容
        :param css:
        :param text:
        :return:
        """
        try:
            ele = self.find_element(css)
            ele.send_keys(text)
        except Exception as msg:
            raise msg

    def open(self, url):
        """
        打开一个网站
        :param url:
        :return:
        """
        try:
            self.driver.get(url)
        except Exception as msg:
            print(msg)

    def max_windows(self):
        """
        最大化浏览器
        :return:
        """
        self.driver.maximize_window()

    def set_widows_size(self, w, h):
        """
        设置当前浏览器的宽度和高度
        :param w: 宽度
        :param h: 高度
        :return:
        """
        self.driver.set_window_size(w, h)

    def current_title(self):
        return self.driver.title

    def current_url(self):
        return self.driver.current_url

    def current_handle(self):
        return self.driver.current_window_handle

    def get_handles(self):
        return self.driver.window_handles

    def get_screen(self, filename):
        self.driver.get_screenshot_as_file(filename)

    def implicit_wait(self, timeout):
        self.driver.implicitly_wait(timeout)

    def execute_js(self, js):
        """
        在当前页面同步执行js
        :param js:
        :return:
        """
        try:
            self.driver.execute_script(js)
        except Exception as msg:
            raise msg

    def execute_async_js(self, js):
        """
        在当前页面异步执行js
        :param js:
        :return:
        """
        try:
            self.driver.execute_async_script(js)
        except Exception as msg:
            raise msg

    def to_frame(self, frame):
        """
        进入frame框架
        :param frame:
        :return:
        """
        try:
            self.driver.switch_to.frame(frame)
        except Exception as msg:
            raise msg

    def to_default_content(self):
        """
        退出当前frame框架
        :return:
        """
        try:
            self.driver.switch_to.default_content()
        except Exception as msg:
            raise msg

    def to_alert(self):
        """
        返回焦点对象
        :return:
        """
        return self.driver.switch_to.alert()

    def dismiss(self):
        try:
            alert = self.to_alert()
            alert.dismiss()
        except Exception as msg:
            raise msg

    def accept(self):
        alert = self.to_alert()
        alert.accept()

    def close(self):
        """
        关闭当前窗口
        :return:
        """
        self.driver.close()

    def quit(self):
        """
        退出浏览器,并关闭所有窗口
        :return:
        """
        self.driver.quit()

    def move_to_element(self, css):
        """
        移到元素位置悬停
        :param css:
        :return:
        """
        ele = self.find_element(css)
        ActionChains(self.driver).move_to_element(ele).perform()

    def double_click(self, css):
        """
        双击666
        :param css:
        :return:
        """
        ele = self.find_element(css)
        ActionChains(self.driver).double_click(ele).perform()

    def drag_and_drop(self, source, css):
        """
        元素拖拽,从起始元素拖动到目标元素
        :param source: 起始元素
        :param css: 目标元素
        :return:
        """
        start_ele = self.find_element(source)
        stop_ele = self.find_element(css)
        ActionChains(self.driver).drag_and_drop(start_ele, stop_ele).perform()

    def context_click(self, css):
        """
        指定元素鼠标右击
        :param css:
        :return:
        """
        ele = self.find_element(css)
        ActionChains(self.driver).context_click(ele).perform()

    def click_and_hold(self, css):
        """
        指定元素鼠标左击
        :param css:
        :return:
        """
        ele = self.find_element(css)
        ActionChains(self.driver).click_and_hold(ele).perform()

    def option(self):
        pass

    def select_value(self, css, value):
        """
        通过值来改变下拉框的选项
        :param css:
        :param value:
        :return:
        """
        ele = self.find_element(css)
        Select(ele).select_by_value(value)

    def select_index(self, css, index):
        """
        通过索引来改变下拉框的选项
        :param css:
        :param index:
        :return:
        """
        ele = self.find_element(css)
        Select(ele).select_by_index(index)

    def select_text(self, css, text):
        """
        通过标签的文本来改变下拉框的选项
        :param css:
        :param text:
        :return:
        """
        ele = self.find_element(css)
        Select(ele).select_by_visible_text(text)