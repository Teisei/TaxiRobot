# -*- coding:utf-8 -*-

config = {
    'didi': {
        'url': "http://api.udache.com/gulfstream/api/v1/passenger/pGetEstimatePriceCoupon",
        'params': {
            "android_id": "2036d0c23a41b53",
            "appTime": "1471676039174",
            "appversion": "4.4.2",
            "area": "4",
            "bubble_type": "1",
            "businesstype": "263",
            "callcar_type": "0",
            "cancel": "test1783b9c5df1968e582510e8747d6c9a3",
            "car_level_type": "0",
            "car_smooth": "1",
            "channel": "824",
            "city_id": "4",
            "datatype": "1",
            "dviceid": "cff3c23d651e57a5e3cb5126b5697c2e",
            "flier": "1",
            # "fromAddress": "%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%BE%90%E6%B1%87%E5%8C%BA%E9%92%A6%E6%B1%9F%E8%B7%AF333%E5%8F%B7",
            # "fromName": "%E9%92%A6%E6%B1%9F%E5%9B%AD",
            "imei": "867992024356669F4F7DC42811DB73DE5156D178C1AABAB",
            "like_wait": "0",
            "login_flag": "1",
            "maptype": "soso",
            "model": "MX5",
            "networkType": "WIFI",
            "os": "5.1",
            "pixels": "1080*1920",
            "pool_seat": "0",
            "tip": "0",
            # "toAddress": "%E9%BB%84%E6%B5%A6%E5%8C%BA%E4%B8%AD%E5%B1%B1%E4%B8%9C%E4%B8%80%E8%B7%AF13%E5%8F%B7",
            # "toName": "%E5%A4%96%E6%BB%A9",
            "type": "0",
            "user_type": "0",
            "vcode": "150",
            "versionid": "37000",
        },
        'header': {
            "User-Agent": "Android/5.1 com.sdu.didi.psnger/4.4.2",
            "Host": "api.udache.com",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "Accept-Language": "zh"
        }
    },
    'uber': {
        'url_price': 'https://api.uber.com.cn/v1/estimates/price',
        'url_time': 'https://api.uber.com.cn/v1/estimates/time',
        'params': {
            'server_token': 'V0FOwsKs-DgoofNelzCRRV88H5RvmaHM4sTKSslk'
        },
        'headers': {
            'Content-Type': 'application/json'
        }
    },
    'yidao': {
        'url': 'http://3g.yongche.com/ajax/get_predict_cost.php',
        'params': {
            "city": "sh",
            "carTypeId": "37",
            "productTypeId": "1",
            "_": "1471694236112"
        },
        'headers': {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13E188a Safari/601.1",
            "X-Requested-With": "XMLHttpRequest",
            "Origin": "http://3g.yongche.com"
        }

    },
    'shenzhou': {
        'url_oauth': 'https://sandboxoauth.10101111.com/oauth/token?client_id=6DF15DDC00000D0A&client_secret=rzixekrhxlhyo1debk49&grant_type=client_credentials',
        'url_price': 'https://sandboxapi.10101111.com/v1/resource/common/estimate/price',
        'url_nearby': 'https://sandboxapi.10101111.com/v1/resource/common/getNearbyCarInfo',
        'params': {
            'serviceId': '14'
        }
    }
}

mock_data = {
    "fromAddress": "%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%BE%90%E6%B1%87%E5%8C%BA%E9%92%A6%E6%B1%9F%E8%B7%AF333%E5%8F%B7",
    "fromName": "%E9%92%A6%E6%B1%9F%E5%9B%AD",
    "toAddress": "%E9%BB%84%E6%B5%A6%E5%8C%BA%E4%B8%AD%E5%B1%B1%E4%B8%9C%E4%B8%80%E8%B7%AF13%E5%8F%B7",
    "toName": "%E5%A4%96%E6%BB%A9",
    'start_latitude': 31.193824167211297,
    'start_longitude': 121.33244751040375,
    'end_latitude': 31.19882056907011,
    'end_longitude': 121.43771418515428
}
# 易道
# "city":"sh"
# "carTypeId":"37"
# "productTypeId":"1"
# "startLat":"31.178256"
# "startLng":"121.400564"
# "endLat":"31.250278"
# "endLng":"121.490664"
# "_":"1471694236112"
