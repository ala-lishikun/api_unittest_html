# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import conf.config
import unittest,os
import time
from HTMLTestRunner import  HTMLTestRunner
import smtplib
from email.mime.text import MIMEText            #MIMRText()定义邮件正文
from email.mime.multipart import MIMEMultipart #MIMEMulipart模块构造带附件


def send_mail(file_new):
    c = conf.config.Config().get_conf()
    #multpart有三种类型，如果一个邮件有纯文本正文，超文本正文，内嵌资源，附件，则选择mixed类型
    msg = MIMEMultipart('mixed')
    #邮箱标题+发件人+收件人
    Subject = '_ala_接口自动化测试报告'
    msg['Subject'] = Subject
    msg['From'] = c["sender"]
    smtpserver = c["smtpserver"]
    #接收者，可以多个
    receiver = c["receiver"]
    msg['To'] = ';'.join(receiver)
    username = c["eusername"]
    password = c["epassword"]

    #邮箱正文
    text = "Hi,附件是测试报告，请使用浏览器打开查看!"
    text_plain = MIMEText(text, 'plain', 'utf-8')
    msg.attach(text_plain)
    #邮箱附件
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    file = MIMEText(mail_body, 'base64', 'utf-8')
    file['Content-type'] = 'application/cttet-strem'
    file["Content-Disposition"] = "attachment;filename = test_report.html"
    msg.attach(file)
    #开启邮箱服务
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username,password)
    smtp.sendmail(username,receiver,msg.as_string())
    #msg：发送消息：邮件内容。一般是msg.as_string():as_string()是将msg(MIMEText对象或者MIMEMultipart对象)变为str。
    smtp.quit()
def new_report(test_report):
    #获取最新测试生成的测试报告
    lists = os.listdir(test_report)
    lists.sort(key=lambda fn:os.path.getmtime(test_report+'\\'+fn))
    file_new = os.path.join(test_report,lists[-1])
    return file_new
if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    #测试报告路径
    test_report = "D:\\PycharmProjects\\Request_test\\Report"
    #测试case所在目录
    test_dir = 'D:\\PycharmProjects\\Request_test\\test_case'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    filename = "D:\\PycharmProjects\\Request_test\\report\\" + now + 'test_report.html'
    fp = open(filename,"wb")
    #生成html的测试报告
    runner = HTMLTestRunner(stream= fp,title = "搜索接口测试报告",description="测试用例执行概况", tester="ala")
    runner.run(discover)
    fp.close()
    new_report = new_report(test_report)
    send_mail(new_report)
    if send_mail:
        print "邮件已发出"
    else:
        print "发送失败"


