# -*- coding:utf-8 -*-

"""
Created by haven on 16/8/20.
"""

import unittest
import uberApi
import yidaoApi
import didiApi
import shenzhou
from config import mock_data


class mytest(unittest.TestCase):
    ##初始化工作
    def setUp(self):
        self.sz_token = shenzhou.getToken()
        pass
        # 退出清理工作

    def tearDown(self):
        pass
        # 具体的测试用例，一定要以test开头

    def test_get_didi_price(self):
        ret = didiApi.get_price(mock_data['start_latitude']
                                     , mock_data['start_longitude']
                                     , mock_data['end_latitude']
                                     , mock_data['end_longitude'])

        print(ret)

    def test_get_uber_price(self):
        ret = uberApi.get_uber_price(mock_data['start_latitude']
                                     , mock_data['start_longitude']
                                     , mock_data['end_latitude']
                                     , mock_data['end_longitude'])
        print(ret)

    def test_get_uber_time(self):
        ret = uberApi.get_uber_time(mock_data['start_latitude']
                                    , mock_data['start_longitude']
                                    , mock_data['end_latitude']
                                    , mock_data['end_longitude'])
        print(ret)

    def testyidao(self):
        ret = yidaoApi.get_price(mock_data['start_latitude']
                                 , mock_data['start_longitude']
                                 , mock_data['end_latitude']
                                 , mock_data['end_longitude'])
        print ret

    def test_sz_price(self):
        ret = shenzhou.get_price(mock_data['start_latitude']
                                 , mock_data['start_longitude']
                                 , mock_data['end_latitude']
                                 , mock_data['end_longitude'], self.sz_token)
        self.assertIsNotNone(ret, "shen zhou price")
        print ret

    def test_sz_nearby(self):
        ret = shenzhou.getNearby(mock_data['start_latitude']
                                 , mock_data['start_longitude']
                                 , self.sz_token)
        self.assertIsNotNone(ret, "shen zhou near")
        print ret

        # self.
        # def testsum(self):
        #     self.assertEqual(myclass.sum(1, 2), 2, 'test sum fail')
        #
        # def testsub(self):
        #     self.assertEqual(myclass.sub(2, 1), 1, 'test sub fail')


if __name__ == '__main__':
    unittest.main()
