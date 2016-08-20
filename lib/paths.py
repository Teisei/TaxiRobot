#!/usr/bin/env python
# coding: utf-8


from RouteCompare import comparePrice
from RouteCompare import utils
import requests


def get_simulate_from():
    return "place a"


def get_simulate_to():
    return "place b"


# def get_paths(place_a, place_b):
#     # paths = dict()
#     # paths['didi'] =
#     return {
#         'price': {
#             'alone': [
#                 {'name': 'uber', 'price': '23.4'}
#                 , {'name': 'didi', 'price': '12'}
#             ]
#         }
#     }
# from_lon_lat=0
# to_lon_lat=0


def get_paths(from_addr, to_addr):
    from_lon_lat = utils.getLonLat(from_addr)
    print from_lon_lat
    to_lon_lat = utils.getLonLat(to_addr)
    print to_lon_lat
    ret = comparePrice.getPath(from_lon_lat[1], from_lon_lat[0], to_lon_lat[1], to_lon_lat[0])
    print ret
    return ret


# get_paths('上海市徐汇区漕河泾', '上海市长宁区长宁路780')


def get_direction(from_addr, to_addr):
    from_lon_lat = utils.getLonLat(from_addr)
    to_lon_lat = utils.getLonLat(to_addr)
    params = {
        'origin': '{0},{1}'.format(from_lon_lat[1], from_lon_lat[0]),
        'destination': '{0},{1}'.format(to_lon_lat[1], to_lon_lat[0]),
        'region': from_addr[0:2],
        'origin_region': from_addr[0:2],
        'destination_region': from_addr[0:2],
        'output': 'json',
        'ak': 'CF0b40357871f4f37b6063537501ae54'
    }
    res = requests.get("http://api.map.baidu.com/direction/v1", params=params).json()

    ret=[]
    for step in res['result']['routes'][0]['steps']:
        ret.append(step['stepOriginLocation'])

    return ret


get_direction('上海市徐汇区漕河泾', '上海市长宁区长宁路780')
