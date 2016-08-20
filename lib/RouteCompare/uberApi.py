# -*- coding:utf-8 -*-

"""
Created by haven on 16/8/20.
"""

import requests
from  config import config


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
