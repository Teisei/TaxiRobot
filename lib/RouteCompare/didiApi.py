# -*- coding:utf-8 -*-

"""
Created by haven on 16/8/20.
"""
from config import config
import requests

import utils


def requestDidi():
    # login_data = {"username": username, "password": password, "action": 'login', 'ajax': '1', 'ac_id': '4'}
    header = config['didi']['header']
    url = config['didi']['url']
    params = config['didi']['params']
    r = requests.get(url, params=params, headers=header)
    print(r.text, r.status_code)


def get_price(from_lat, from_lon, to_lat, to_lon):
    header = config['didi']['header']
    url = config['didi']['url']
    params = {
        'userlat': from_lat,
        'userlng': from_lon,
        'flat': from_lat,
        'flng': from_lon,
        'tlat': to_lat,
        'tlng': to_lon
        # 'appTime': utils.getUnixTime()
    }
    # print params
    params = dict(params, **config['didi']['params'])

    # print url
    # print params
    # print header
    ret = requests.get(url, params=params, headers=header).json()

    estimate_fee_data = ret['estimate_fee_data']
    if 'time_cost' in estimate_fee_data:
        time_cost = estimate_fee_data[0]['time_cost']
    else:
        time_cost = -1
    if 'distance' in estimate_fee_data:
        distance = estimate_fee_data[0]['distance']
    else:
        distance = -1

    return {
        'single_price': float(ret['estimateFee_num'])+4,
        'pool_price': -1,
        'distance': distance,
        'duration': int(time_cost) * 60,
        'name': 'didi',
        'wait_time': utils.get_int(ret['arriveTimeTips']) * 60
    }

# requestDidi()
