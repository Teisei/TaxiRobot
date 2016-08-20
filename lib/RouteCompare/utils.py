# -*- coding:utf-8 -*-

"""
Created by haven on 16/8/20.
"""
import requests


def getUnixTime():
    pass


'''
@:return u'121.386620,31.171283'
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
    location =  res.json()['result']['location']
    return list(map(lambda x: int(x), [location['lng'],location['lat']]))


# getLonLat('上海市闵行区万源路2289弄1-39号')
