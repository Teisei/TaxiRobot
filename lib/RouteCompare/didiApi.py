# -*- coding:utf-8 -*-

"""
Created by haven on 16/8/20.
"""
from config import config
import requests


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
    didi = config['didi']['params']
    params = {
        'userlat': from_lat,
        'userlng': from_lon,
        'flat': from_lat,
        'flng': from_lon,
        'tlat': to_lat,
        'tlng': to_lon
    }
    # print params
    params = dict(params, **config['didi']['params'])

    ret = requests.get(url, params=params, headers=header)
    return ret.json()

# requestDidi()
