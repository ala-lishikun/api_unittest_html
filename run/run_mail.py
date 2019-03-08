# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import unittest,os
import time
from HTMLTestRunner import  HTMLTestRunner
import smtplib
from email.mime.text import MIMEText
from email.header import Header
def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header('_ala_接口自动化测试报告', 'utf-8')
    msg['From'] = 'ala'

    msg['To']  = 'ala'
    smtp = smtplib.SMTP()
    smtp.connect('smtp.ala.com')
    smtp.login('lishikun@ala.com','PASSWORD')
    smtp.sendmail('lishikun@ala.com','lishikun@ala.com',msg.as_string())
    smtp.quit()
    print('邮件已发出！注意查收。')
def new_report(test_report):
    lists = os.listdir(test_report)
    lists.sort(key=lambda fn:os.path.getmtime(test_report+'\\'+fn))
    file_new = os.path.join(test_report,lists[-1])
    return file_new
if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    test_report = "D:\\PycharmProjects\\LV_BG\\LvWan\\Request_test\\report"
    test_dir = 'D:\\PycharmProjects\\LV_BG\\LvWan\\Request_test\\test_case'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    filename = "D:\\PycharmProjects\\LV_BG\\LvWan\\Request_test\\report\\" + now + 'test_report.html'
    fp = open(filename,"wb")
    runner = HTMLTestRunner(stream= fp,
                            title = "搜索接口测试报告",
                            description="测试用例执行概况",
                            tester="ala")
    runner.run(discover)
    fp.close()
    new_report = new_report(test_report)
    send_mail(new_report)

