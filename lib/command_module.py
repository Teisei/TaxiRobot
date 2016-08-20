#!/usr/bin/env python
# coding: utf-8
def getRequest(content):
    result = {}
    if str_contains(content, '1'):
        result['type'] = 'command'
        result['value'] = 'dache'

    elif str_contains(content, '2'):
        result['type'] = 'command'
        result['value'] = 'dengche'

    elif str_contains(content, '3'):
        result['type'] = 'command'
        result['value'] = 'anquan'

    elif str_contains(content, '4'):
        result['type'] = 'location'
        result['value'] = content

    elif str_contains(content, '0'):
        result['type'] = 'reset'
        result['value'] = content

    else:
        result['type'] = 'command'
        result['value'] = content
    return result

def str_contains(sStr1, sStr2):
    return sStr1.find(sStr2) > -1

print str_contains('woyaodache', 'dache')

