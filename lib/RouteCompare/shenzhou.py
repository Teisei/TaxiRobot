# -*- coding:utf-8 -*-

"""
Created by haven on 16/8/20.
"""
import requests
from  config import config

'''
@:return {u'access_token': u'92bdccfc-13bd-4c5c-9454-28d4344929a2', u'token_type': u'bearer', u'expires_in': 42641, u'scope': u'read'}
'''

from Dache import Dache
import time
import utils


class ShenZhou(Dache):
    def __init__(self, from_lat, from_lon, to_lat, to_lon):
        # Dache.__init__(self)
        # super(from_lat, from_lon, to_lat, to_lon)
        super(ShenZhou, self).__init__(from_lat, from_lon, to_lat, to_lon)
        self.config = config['shenzhou']

        ret = requests.post(self.config['url_oauth'])
        token = ret.json()['access_token']

        self.params = {
            'slat': from_lat,
            'slng': from_lon,
            'elat': to_lat,
            'elng': to_lon,
            'access_token': token,
            'departureTime': utils.getUnixTime(),
            'name': 'shenzhou'
        }
        self.params = dict(self.params, **self.config['params'])

    def price(self):
        print self.params
        # print self.config['url_price']
        ret = requests.get(self.config['url_price'], params=self.params).json()
        print ret
        return {
            'single_price': ret['content']['prices'][0]['price'],
            'pool_price': -1,
            'distance': float(ret['content']['distance']) / 1000,
            'duration': int(ret['content']['duration']) * 60,
            'name':'shenzhou'
        }

    def time(self):
        ret = requests.get(self.config['url_time'], params=self.params).json()
        print ret
        return {
            'wait_time': int(ret['content']['shortestTimeOfArrival']) * 60
        }

    def get_info(self):
        return dict(self.price(), **self.time())


def getToken():
    sz = config['shenzhou']
    # params={
    #     "client_id": "6DF15DDC00000D0A",
    #     "client_secret": "rzixekrhxlhyo1debk49",
    #     "grant_type": "client_credentials"
    # }
    ret = requests.post(sz['url_oauth'])
    return ret.json()['access_token']


def get_price(from_lat, from_lon, to_lat, to_lon, token=None):
    if not token:
        token = getToken()
    sz = config['shenzhou']
    params = {
        'slat': from_lat,
        'slng': from_lon,
        'elat': to_lat,
        'elng': to_lon,
        'access_token': token
    }
    params = dict(params, **sz['params'])
    # print params
    ret = requests.get(sz['url_price'], params=params)

    return ret.json()


# shortestTimeOfArrival
def getNearby(from_lat, from_lon, token=None):
    if not token:
        token = getToken()
    sz = config['shenzhou']
    params = {
        'slat': from_lat,
        'slng': from_lon,
        'access_token': token
    }
    # print params
    ret = requests.get(sz['url_nearby'], params=params)
    return ret.json()

# getToken()
