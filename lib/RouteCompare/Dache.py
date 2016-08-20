# -*- coding:utf-8 -*-

"""
Created by haven on 16/8/21.
"""


class Dache(object):
    def __init__(self, from_lat, from_lon, to_lat, to_lon):
        self.from_lat = from_lat
        self.from_lon = from_lon
        self.to_lat = to_lat
        self.to_lon = to_lon

    '''
    @:return {
        'single':2,
        'pool':1,
        'distance':1, km
        'duration':1   sec
    }
    '''

    def price(self):
        pass

    def time(self):
        pass
