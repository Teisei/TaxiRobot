#!/usr/bin/env python
# coding: utf-8

import re
import json

locations = r'(.*)\:.*(location)$'
numbers = r'.*(\d{11}).*'
fournums = r'.*(\d{4}).*'
reset = r'(0)'
orders = r'.*xml.*\<title\>.*'

dache = r'.*(打车|dache|da车|打che).*'
dengche = r'.*(等车|deng车|等che|dengche).*'
anquan = r'.*(安全).*'

commands = {dache: 'dache', dengche: 'dengche', anquan: 'anquan', reset: 'reset'}

def getRequest(content):
    print content
    # 地址
    reloc = re.match(locations, content)
    if (reloc):
        request = {}
        request['type'] = 'location'
        request['value'] = reloc.group(1)
        return json.dumps(request)
    #订单
    reorder = re.match(orders, content)
    if (reorder):
        request = {}
        request['type'] = 'order'
        request['value'] = content
        return json.dumps(request)
    # 号码
    renum = re.match(numbers, content)
    if (renum):
        request = {}
        request['type'] = 'number'
        request['value'] = renum.group(1)
        return json.dumps(request)
    # 4位号码
    refour = re.match(fournums,content)
    if(refour):
        request = {}
        request['type'] = 'number'
        request['value'] = refour.group(1)
        return json.dumps(request)
    # 命令
    for command in commands:
        if (re.match(command, content)):
            request = {}
            request['type'] = 'command'
            request['value'] = commands[command]
            return json.dumps(request)

    request = {}
    request['type'] = 'other'
    request['value'] = content
    return json.dumps(request)