# _author_='shaojie'
# -*- coding:utf-8 -*-

import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Send(object):

    def __init__(self):
        self.msg = MIMEMultipart()  # Creates a multipart/* type message
        self.msg['Subject'] = '主题'
        self.msg['From'] = '发送人'
        self.msg['To'] = '接收人'

    def add_accessory(self, file):
        part = MIMEText('正文')   # Create a text/* type MIME document
        self.msg.attach(part)  # 添加到负载
        with open(file, 'w') as f:
            msg = f.read()
        accessory = MIMEApplication(msg)  # Create an application/* type MIME document
        accessory.add_header('content-disposition', 'attachment', filename='自动化测试报告.html')  # 设置标题
        self.msg.attach(accessory)

    def send_email(self):
        try:
            s = smtplib.SMTP_SSL()  # 创建一个STMP连接服务器的对象
            s.login('user', 'password')
            s.sendmail('发送人', '接收人', self.msg)
            s.quit()
        except Exception as msg:
            print('邮件发送失败,失败原因:%s' % msg)
