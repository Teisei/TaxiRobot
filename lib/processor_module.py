#!/usr/bin/env python
# coding: utf-8
import os
import sys
import kvstore_module
from paths import *


path_prepend = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'lib')
sys.path.append(path_prepend)
import log
log.Logs.set_context(directory='./', namespace='robot')
logger = log.Logs().get_logger('weixinBot')


def process(command, context):
    return 'this is the result'


def return_default():
    return u'I dont understand!'


def view_message(msg):
    msgType = msg['MsgType']
    FromUserName = msg['FromUserName']
    content = msg['Content'].replace('&lt;', '<').replace('&gt;', '>')
    msgid = msg['MsgId']
    print 'msgType: ' + str(msgType)
    print 'msgType: ' + str(FromUserName)
    print 'content: ' + str(content)
    print 'msgid: ' + str(msgid)


def main_process(weixin, name, request):
    context = kvstore_module.get_Context(name)
    type = request['type']
    value = request['value']

    logger.info(name + '\t' + type + '\t' + value)

    if type == 'command':
        command = value
        if command == 'dache':
            # TODO
            deal_dache(weixin, name, value, context)

        elif command == 'dengche':
            # TODO
            deal_dengche(weixin, name, value, context)

        elif command == 'anquan':
            # TODO
            deal_anquan(weixin, name, value, context)

        else:
            deal_unknown(weixin, name, value, context)

    elif type == 'location':
        deal_localtion(weixin, name, value, context)

    elif type == 'reset':
        deal_reset(weixin, name, value, context)

    else:
        pass


def deal_localtion(weixin, name, location, context):
    result = ''
    if 'place_a' in context and context['place_a'] != '':
        if 'place_b' in context and context['place_a'] != '':
            # you have a plan already, do you want a another plan?]
            if 'reset_location' in context and context['reset_location'] != '':
                context['place_a'] = location
                result += 'reset the depart from: %s\n' % location
            else:
                place_a = context['place_a']
                place_b = context['place_b']
                result += 'you have plan already: %s, we reset it?\n' % str_from_to(place_a, place_b)
                context['reset_location'] = 'yes'
        else:
            context['place_b'] = location
            result += 'set destination to: %s!\n' % location
            result += str(get_paths(context['place_a'], context['place_b']))
    else:
        # set the start place
        context['place_a'] = location
        result += 'set depart from: %s!\n' % location

    kvstore_module.set_Context(name, context)
    weixin.sendMsg(name, result)

def deal_reset(weixin, name, value, context):
    if 'place_a' in context:
        context.pop('place_a')
    if 'place_b' in context:
        context.pop('place_b')
    if 'status' in context:
        context.pop('status')
    result = 'reset configuration successfully!'
    kvstore_module.set_Context(name, context)
    weixin.sendMsg(name, result)


def deal_dache(weixin, name, value, context):
    result = ''
    if 'place_a' in context:
        if 'place_b' in context:
            place_a = context['place_a']
            place_b = context['place_b']
            result += 'current plan:\n %s, \npress 0 to reset.' % str_from_to(place_a, place_b)
            context['step'] = 'from'
        else:
            result += 'qin, input where to go?\n'
    else:
        result += 'please input where you are from?\n'

    kvstore_module.set_Context(name, context)
    weixin.sendMsg(name, result)


def deal_dengche(weixin, name, value, context):
    word = 'wo zai deng che!'
    weixin.sendMsg(name, word)


def deal_anquan(weixin, name, value, context):
    word = 'wo yao an quan!'
    weixin.sendMsg(name, word)


def deal_unknown(weixin, name):
    word = 'I dont understand!'
    weixin.sendMsg(name, word)


def str_from_to(place_a, place_b):
    return '(' + place_a + ') --> (' + place_b + ')'
