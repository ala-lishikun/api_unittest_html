# -*- coding: utf-8 -*-

import unittest
import conf.config
import requests
import time
from HTMLTestRunner import HTMLTestRunner
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
#定义测试用例的目录
test_dir = 'D:\\PycharmProjects\\Ala_test\\test_case'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*.py')

if __name__ == '__main__':

    now = time.strftime("%Y-%m-%d %H_%M_%S")

    filename = "D:\\Report\\" + now + 'test_report.html'
    fp = open(filename, "wb")

    runner = HTMLTestRunner(stream=fp,
                            title="搜索接口测试报告",
                            description="测试用例执行概况",
                            tester="阿拉")
    runner.run(discover)
    fp.close()

