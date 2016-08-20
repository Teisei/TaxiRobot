#!/usr/bin/env python
# coding: utf-8


from RouteCompare import comparePrice
from RouteCompare import utils


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

def get_paths(from_addr, to_addr):
    from_lon_lat = utils.getLonLat(from_addr)
    print from_lon_lat
    to_lon_lat = utils.getLonLat(to_addr)
    print to_lon_lat
    ret = comparePrice.getPath(from_lon_lat[1], from_lon_lat[0], to_lon_lat[1], to_lon_lat[0])
    print ret
    return ret

#get_paths('上海市徐汇区漕河泾','上海市浦东新区迎宾大道6000号')
