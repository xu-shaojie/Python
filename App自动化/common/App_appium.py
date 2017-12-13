# _author_='shaojie'
# -*- coding:utf-8 -*-

from appium import webdriver
from appium.webdriver.connectiontype import ConnectionType


class MyTest(object):

    def __init__(self):
        self.driver = webdriver.Remote()

    def find_element(self, css):
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

    def find_elements(self, css):
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

    def click(self, css):
        """
        点击某个元素
        :param css:
        :return:
        """
        ele = self.find_element(css)
        ele.click()

    def send_keys(self, css, text):
        """
        发送文本 or 按键
        :param css:
        :param text:
        :return:
        """
        ele = self.find_element(css)
        ele.send_keys(text)

    def clear(self, css):
        """
        清除文本框内容
        :param css:
        :return:
        """
        ele = self.find_element(css)
        ele.clear()

    def submit(self, css):
        """
        表单提交
        :param css:
        :return:
        """
        self.find_element(css).submit()

    def location(self,css,reference):
        """
        获取当前元素的x or y坐标 可搭配swipe,scroll使用更佳
        :Usage: self.location("id->kw","x")
        :param css: 元素
        :param reference: x or y
        :return:
        """
        ele = self.find_element(css)
        return ele.location.get(reference)

    def tap(self, position, timeout):
        """
        模拟手指点击
        :param position: 位置
        :param timeout: 点击时间
        :return:
        """
        self.driver.tap(position, timeout)

    def swipe(self,start_x, start_y, end_x, end_y, timeout=None):
        """
        从起点滑动到终点 A-B
        :param start_x: 起始位置的横坐标x
        :param start_y: 起始位置的纵坐标y
        :param end_x:   结束位置的横坐标x
        :param end_y:   结束位置的纵坐标y
        :param timeout: 持续时间
        :return:
        """
        self.driver.swipe(start_x, start_y, end_x, end_y, timeout)

    def scroll(self, start_css, end_css):
        """
        从A滚动到B
        :param start_css: 起始元素A
        :param end_css:   结束元素B
        :return:
        """
        start_ele = self.find_element(start_css)
        end_ele = self.find_element(end_css)
        self.driver.scroll(start_ele, end_ele)

    def flick(self, start_x, start_y, end_x, end_y):
        """
        从起点快速滑动到终点
        :param start_x: 起始位置的横坐标x
        :param start_y: 起始位置的纵坐标y
        :param end_x:  结束位置的横坐标x
        :param end_y: 结束位置的纵坐标y
        :return:
        """
        self.driver.flick(start_x, start_y, end_x, end_y)

    def drag_and_drop(self, start_css, end_css):
        """
        从A元素拖到到B元素
        :param start_css: 起始A元素
        :param end_css:   结束B元素
        :return:
        """
        start_ele = self.find_element(start_css)
        end_ele = self.find_element(end_css)
        self.driver.drag_and_drop(start_ele, end_ele)

    def background_app(self, timeout):
        """
        后台运行app
        :param timeout: 运行时间
        :return:
        """
        self.driver.background_app(timeout)

    def install_app(self,app_path):
        """
        安装App
        :param app_path: App的存放地址,切记只可安装,不可覆盖
        :return:
        """
        self.driver.install_app(app_path)

    def remove_app(self,app_id):
        """
        卸载App
        :param app_id: App的包名
        :return:
        """
        self.driver.remove_app(app_id)

    def is_app(self, app_id):
        """
        检查App是否安装,返回True/False
        :param app_id:
        :return:
        """
        return self.driver.is_app_installed(app_id)

    def quit(self):
        """
        退出appium程序，并关闭App
        :return:
        """
        self.driver.quit()

    def close_app(self):
        """
        关闭App程序
        :return:
        """
        self.driver.close_app()

    def launch_app(self):
        """
        启动App程序
        :return:
        """
        self.driver.launch_app()

    def reset(self):
        """
        重置当前的App
        :return:
        """
        self.driver.reset()

    def key_event(self, key_code, meta_state=None):
        """
        发送按键
        简书按键地址:http://www.jianshu.com/p/71c3608de453
        :param key_code: 按键
        :param meta_state:
        :return:
        """
        self.driver.keyevent(key_code, meta_state)

    def shake(self):
        """
        手机摇一摇
        :return:
        """
        self.driver.shake()

    def set_network(self,connection):
        """
        设置网络模式
         Possible values:
        Value (Alias)      | Data | Wifi | Airplane Mode
        -------------------------------------------------
        0 (None)           | 0    | 0    | 0
        1 (Airplane Mode)  | 0    | 0    | 1
        2 (Wifi only)      | 0    | 1    | 0
        4 (Data only)      | 1    | 0    | 0
        6 (All network on) | 1    | 1    | 0
        :param connection:
        :return:
        """
        if connection == "0":
            connection_type = ConnectionType.NO_CONNECTION
        elif connection == "1":
            connection_type = ConnectionType.AIRPLANE_MODE
        elif connection == "2":
            connection_type = ConnectionType.WIFI_ONLY
        elif connection == "4":
            connection_type = ConnectionType.DATA_ONLY
        elif connection == "6":
            connection_type = ConnectionType.ALL_NETWORK_ON
        else:
            print('输入错误....')
            connection_type = None
        self.driver.set_network_connection(connection_type)

    def toggle_location(self):
        """
        打开定位服务
        :return:
        """
        self.driver.toggle_location_services()

    def open_notifications(self):
        """
        打开通知栏
        :return:
        """
        self.driver.open_notifications()

    def get_contexts(self):
        """
        返回当前会话中的上下文，使用后可以识别H5页面的控件
        :return:
        """
        return self.driver.contexts

    def get_current_context(self):
        """
        返回当前的上下文
        :return:
        """
        return self.driver.current_context

    def get_network_type(self):
        """
        返回网络类型
        :return:
        """
        return self.driver.network_connection

    def current_url(self):
        """
        获取当前h5的url
        :return:
        """
        return self.driver.current_url

    def current_window_handle(self):
        """
        返回当前的窗口句柄(handle)
        :return:
        """
        return self.driver.current_window_handle

    def current_activity(self):
        """
        获取当前的activity
        :return:
        """
        return self.driver.current_activity

    def lock(self, timeout):
        """
        后台运行(IOS独有)
        :param timeout: 持续时间
        :return:
        """
        self.driver.lock(timeout)

    def start_activity(self, app_page, app_activity):
        """
        启动其他App的应用程序(安卓独有)
        :param app_page: App包名
        :param app_activity: App启动activity
        :return:
        """
        self.driver.start_activity(app_page, app_activity)

    def wait_activity(self, activity, timeout):
        """
        等待指定的activity出现,直到超时,扫描间隔为1s
        :param activity: activity名
        :param timeout: 超时时间
        :return:
        """
        self.driver.wait_activity(activity, timeout,interval=1)

    def get_screen_shot_as_file(self, filename):
        """
        截取当前窗口的截图保存
        :param filename: 错误截图的地址
        :return:
        """
        self.driver.get_screenshot_as_file(filename)

    def execute_script(self,js):
        """
        同步执行js代码
        :param js:
        /*
        在当前窗口/框架（特指Html的iframe）
        同步执行 javascript 代码。
        你可以理解为如果这段代码是睡眠5秒，
        这五秒内主线程的 javascript 不会执行
        */
        :return:
        """
        self.driver.execute_script(js)

    def execute_async_script(self,js):
        """
        异步执行js代码
        :param js:
        /*
        插入 javascript 代码，只是这个是异步的，
        也就是如果你的代码是睡眠5秒，
        那么你只是自己在睡，
        页面的其他 javascript代码还是照常执行
        */
        :return:
        """
        self.driver.execute_async_script(js)