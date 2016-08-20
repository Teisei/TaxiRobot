# -*- coding:utf-8 -*-

"""
Created by haven on 16/8/20.
"""
import requests
from  config import config

import re

def get_price(from_lat, from_lon, to_lat, to_lon):
    yidao = config['yidao']
    # print yidao['headers']
    params = {
        'startLat': round(from_lat, 6),
        'startLng': round(from_lon, 6),
        'endLat': round(to_lat, 6),
        'endLng': round(to_lon, 6)
    }
    # print params
    params = dict(params, **yidao['params'])
    # print params
    ret = requests.get(yidao['url'], params=params, headers=yidao['headers']).json()
    # print ret
    print ret
    return {
        'single_price': ret['result']['total_fee'],
        'pool_price': -1,
        'distance': ret['result'][u'公里费'] / ret['result'][u'公里单价'],
        'duration': int(re.findall(r"\d+",ret['time_length_detail'])[0])*60,
        'name': 'yidao'
    }


'''
{
  "code": 200,
  "msg": "",
  "result": {
    "最小消费金额": 13,
    "起步价": 1,
    "实际计费分钟": 31,
    "实际计费公里数": 15.02,
    "超出分钟": 31,
    "超时费": 9.3,
    "超公里费": 30.04,
    "长途服务公里数": 3.02,
    "长途服务费": 3.02,
    "夜间服务费": 0,
    "原始订单基本费用": 43.36,
    "订单加价金额": 0,
    "订单基本费用": 43.36,
    "高速费": 0,
    "停车费": 0,
    "其他费用": 0,
    "优惠券折扣": 1,
    "限扣券基本费用": 0,
    "限扣券金额": 0,
    "满减券上限金额": 0,
    "满减券金额": 0,
    "减免金额": 0,
    "会员折扣": 1,
    "折扣": 1,
    "订单原始金额": 43,
    "订单优惠后金额": 43.36,
    "订单优惠金额": 0,
    "取消订单金额": 0,
    "用户未付金额": 43.36,
    "应付金额": 43,
    "空驶费": 3.02,
    "时租费": 10.3,
    "固定价格": 1,
    "公里费": 30.04,
    "计费单位": "分钟",
    "时长单价": 30,
    "分钟单价": 0.3,
    "公里单价": 2,
    "长途服务公里单价": 1,
    "免费分钟": "0",
    "免费公里数": "0",
    "时长粒度": "60",
    "时长粒度分钟": 1,
    "夜间服务费单价": 0.5,
    "免费空驶公里数": 12,
    "系统提价倍率": 0,
    "total_fee": 43
  },
  "html_str": "<p class=\"mb20 xs5\">预估费用：<span class=\"c_red2\">43元</span><span class=\"xs2 ml20\">( 预计31 分钟、15.02公里 )</span></p><p class=\"mt5\">起步价：1元（含0 分钟、0公里）</p><p class=\"mt5\">时长费：9.3元（31 分钟、0.3元/分钟）</p><p class=\"mt5\">里程费：30.04元（15.02公里、2元/公里）</p><p class=\"mt5\">长途服务费：3.02元（3.02公里、1元/公里）<em class=\"c_999\" style=\"font-size:12px;\">行程大于0公里部分,每公里收取1元长途服务费</em></p>",
  "html_str_h5": "<div class=\"dis_box pack_justify mb10\"><div>起步价：</div><div>1元</div></div><div class=\"dis_box pack_justify mb10\"><div>时长费：</div><div>9.3元</div></div><div class=\"dis_box pack_justify mb10\"><div>里程费：</div><div>30.04元</div></div><div class=\"dis_box pack_justify mb10\"><div>长途服务费：</div><div>3.02元</div></div>",
  "night_time_length_detail": "0分钟",
  "time_length_detail": "31 分钟",
  "time_length_price": "0.3元/分钟",
  "distance_length_price": "2元/公里"
}
'''
