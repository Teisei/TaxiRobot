# -*- coding:utf-8 -*-

"""
Created by haven on 16/8/20.
"""

import requests
from  config import config

# from Dach import Dache
from Dache import Dache


class Uber(Dache):
    def __init__(self, from_lat, from_lon, to_lat, to_lon):
        # Dache.__init__(self)
        # super(from_lat, from_lon, to_lat, to_lon)
        super(Uber, self).__init__(from_lat, from_lon, to_lat, to_lon)
        self.config = config['uber']
        self.params = {
            'start_latitude': from_lat,
            'start_longitude': from_lon,
            'end_latitude': to_lat,
            'end_longitude': to_lon
        }
        self.params = dict(self.params, **self.config['params'])

    def price(self):
        ret = requests.get(self.config['url_price'], params=self.params, headers=self.config['headers']).json()
        print 'get price'
        return {
            'single_price': (ret['prices'][0]['high_estimate'] + ret['prices'][0]['low_estimate']) / 2,
            'pool_price': (ret['prices'][1]['high_estimate'] + ret['prices'][1]['low_estimate']) / 2,
            'distance': ret['prices'][1]['distance'],
            'duration': ret['prices'][1]['duration'],
            'name':'uber'
        }

    def time(self):
        ret = requests.get(self.config['url_time'], params=self.params, headers=self.config['headers']).json()
        print 'get time'
        return {
            'wait_time': (ret['times'][0]['estimate']+ret['times'][1]['estimate'])/2
        }

    def get_info(self):
        return dict(self.price(), **self.time())


        # return {
        #     'single': (ret['prices'][0]['high_estimate'] + ret['prices'][0]['low_estimate']) / 2,
        #     'pool': (ret['prices'][1]['high_estimate'] + ret['prices'][1]['low_estimate']) / 2,
        #     'distance': ret['prices'][1]['distance'],
        #     'duration': ret['prices'][1]['duration']
        # }


def get_uber_time(from_lat, from_lon, to_lat, to_lon):
    uber = config['uber']
    # print uber
    params = {
        'start_latitude': from_lat,
        'start_longitude': from_lon,
        'end_latitude': to_lat,
        'end_longitude': to_lon
    }
    # print params
    params = dict(params, **uber['params'])
    # print params
    ret = requests.get(uber['url_time'], params=params, headers=uber['headers'])
    return ret.json()


def get_uber_price(from_lat, from_lon, to_lat, to_lon):
    uber = config['uber']
    # print uber
    params = {
        'start_latitude': from_lat,
        'start_longitude': from_lon,
        'end_latitude': to_lat,
        'end_longitude': to_lon
    }
    # print params
    params = dict(params, **uber['params'])
    # print params
    ret = requests.get(uber['url_price'], params=params, headers=uber['headers'])
    # print ret.json()
    return ret.json()
    # return {
    #     'ret':ret.json,
    #     'status':
    # }

#
#
# url = 'https://api.uber.com.cn/v1/estimates/price'
#
# parameters = {
#     # 'Authorization': 'V0FOwsKs-DgoofNelzCRRV88H5RvmaHM4sTKSslk',
#     'server_token': 'V0FOwsKs-DgoofNelzCRRV88H5RvmaHM4sTKSslk',
#     'start_latitude': 31.193824167211297,
#     'start_longitude': 121.33244751040375,
#     'end_latitude': 31.19882056907011,
#     'end_longitude': 121.43771418515428
# }
#
# headers = {
#     # 'Authorization': 'bearer lrY9qKMZqflY-QQe7DWZ0CSwslVgFcn2q6i904j_',
#     'Content-Type': 'application/json'
# }
#
# response = requests.get(url, params=parameters, headers=headers)
#
# data = response.json()
# print(data)
