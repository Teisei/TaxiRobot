# -*- coding:utf-8 -*-

import didiApi
import shenzhou
import uberApi
import yidaoApi
from config import mock_data

"""
Created by haven on 16/8/20.
"""


def getPath(from_lat, from_lon, to_lat, to_lon):
    sz = shenzhou.ShenZhou(from_lat, from_lon, to_lat, to_lon).get_info()
    # print sz


    ub = uberApi.Uber(from_lat, from_lon, to_lat, to_lon).get_info()
    # print ub

    yd = yidaoApi.get_price(from_lat, from_lon, to_lat, to_lon)
    didi = didiApi.get_price(from_lat, from_lon, to_lat, to_lon)

    # print ret

    return [sz, yd, ub, didi]

# getPath(mock_data['start_latitude']
#         , mock_data['start_longitude']
#         , mock_data['end_latitude']
#         , mock_data['end_longitude'])
