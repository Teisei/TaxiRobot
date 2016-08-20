# -*- coding:utf-8 -*-

"""
Created by haven on 16/8/20.
"""
import requests

import datetime
import time
import re


def get_int(str):
    return int(re.findall(r"\d+", str)[0])


def getUnixTime():
    return int(time.mktime(datetime.datetime.now().timetuple()))


'''
@:return u'[121.386620,31.171283]'
            lon,lat
'''


def getLonLat(addr):
    params = {
        'ak': 'CF0b40357871f4f37b6063537501ae54',
        'address': addr,
        'output': 'json'
    }
    res = requests.get("http://api.map.baidu.com/geocoder/v2/", params=params)

    print res.json()
    location = res.json()['result']['location']
    return list(map(lambda x: float(x), [location['lng'], location['lat']]))


def getLatLon(addr):
    params = {
        'ak': 'CF0b40357871f4f37b6063537501ae54',
        'address': addr,
        'output': 'json'
    }
    res = requests.get("http://api.map.baidu.com/geocoder/v2/", params=params)

    print res.json()
    location = res.json()['result']['location']
    return list(map(lambda x: float(x), [location['lat'], location['lng']]))

# getLonLat('上海市闵行区万源路2289弄1-39号')
