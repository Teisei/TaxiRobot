# -*- coding:utf-8 -*-

"""
Created by haven on 16/8/20.
"""
import requests
from  config import config

'''
@:return {u'access_token': u'92bdccfc-13bd-4c5c-9454-28d4344929a2', u'token_type': u'bearer', u'expires_in': 42641, u'scope': u'read'}
'''


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
