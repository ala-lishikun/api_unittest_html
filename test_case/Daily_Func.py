# -*- coding: utf-8 -*-
import requests
import sys,json
import unittest
import Common_Func
import conf.config
reload(sys)
sys.setdefaultencoding("utf-8")


class Daily(unittest.TestCase):
    def setUp(self):
        self.token = Common_Func.Get_token()
        self.c = conf.config.Config().get_conf()

    def tearDown(self):
        pass

    def test_datailview(self):
        URL = self.c['common_url'] + '/selection/detailview'
        #快速浏览
        datailview_data = {
            "objectId": self.c['search_rowkey'], "type": "basicInfo", "category": "", "pageIndex": 0, "pageSize": 10
        }
        headers = {"Content-Type": "application/json", "***-Auth-Token": self.token}
        res = requests.post(url=URL, json=datailview_data, headers=headers)
        print "测试数据:" + str(datailview_data)
        print "返回的内容:" + str(res.text)[0:50]+"....}"
        print "返回状态:" + str(res.json()['code']) + ", 预期状态: 100000"
        assert str(res.json()['code']) == '100000'
        self.assertIn(self.c['search_rowkey'], res.text)
        print "返回值比对通过"
        print "成功打开'" + str(res.json()["data"]["basicInfo"]["name"]) + "'的详情页面"
        print "测试通过"



if __name__ == '__main__':
    unittest.main()

