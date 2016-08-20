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
    sz = shenzhou.get_price(from_lat, from_lon, to_lat, to_lon)
    # print sz

    ub = uberApi.get_uber_price(from_lat, from_lon, to_lat, to_lon)
    # print ub

    yd = yidaoApi.get_price(from_lat, from_lon, to_lat, to_lon)
    didi = didiApi.get_price(from_lat, from_lon, to_lat, to_lon)

    ret = {
        'price': {
            'alone': [
                {'name': 'sz', 'price': sz['content']['prices'][0]['price']}
                , {'name': 'didi', 'price': didi['estimate_fee_data'][0]['estimateFee_num']}
                , {'name': 'uber', 'price': (ub['prices'][0]['high_estimate'] + ub['prices'][0]['low_estimate']) / 2}
                , {'name': 'yd', 'price': yd['result'][u'\u8ba2\u5355\u57fa\u672c\u8d39\u7528']}
            ]
        }
    }

    # print ret

    return ret


# getPath(mock_data['start_latitude']
#         , mock_data['start_longitude']
#         , mock_data['end_latitude']
#         , mock_data['end_longitude'])
