#!/usr/bin/env python
# coding: utf-8
import os

from flask import json

import kvstore_module
from Trace.trace_helper import get_similar_names
from paths import *
import sys
from datetime import datetime

reload(sys)
sys.setdefaultencoding('utf8')

path_prepend = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'lib')
sys.path.append(path_prepend)
import log
from str_map import dache_name

log.Logs.set_context(directory='./', namespace='robot')
logger = log.Logs().get_logger('weixinBot_processor')

# 安全守护
security_message = '如果需要安全守护, 请分享您的打车订单!'


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
    if isinstance(request, str):
        request = json.loads(request)
    type = request['type']
    value = request['value']

    logger.info(name + '\t' + type + '\t' + value)

    if type == 'command':
        command = value
        if command == 'dache':
            deal_dache(weixin, name, value, context)

        elif command == 'dengche':
            # TODO
            deal_dengche(weixin, name, value, context)

        elif command == 'anquan':
            # TODO
            deal_anquan(weixin, name, value, context)
        elif command == 'reset':
            deal_reset(weixin, name, value, context)
        elif commang =='shouye':
            deal_shouye(weixin, name, value, context)
        else:
            deal_unknown(weixin, name, value, context)

    elif type == 'location':
        deal_localtion(weixin, name, value, context)

    elif type == 'number':
        deal_number(weixin, name, value, context)

    elif type == 'order':
        deal_order(weixin, name, value, context)

    else:
        deal_dengche(weixin, name, value, context)

def deal_shouye(weixin, name, value, context):
    result=''
    result='【您好，我是您的出行小助手巴迪，我可以为您提供一条安全实惠的出行路线】' \
           '您可以输入\n------【打车比价】------\n------【等车休闲】-------\n------【安全小护卫】-------\n我们会为您提供相应服务。【为了您的安全考虑，输入【A+手机号码】 自动设置【紧急联系人】'
    weixin.sendMsg(name, result)


def deal_localtion(weixin, name, location, context):
    result = unicode('')
    if 'place_a' in context and context['place_a'] != '':
        if 'place_b' in context and context['place_a'] != '':
            # you have a plan already, do you want a another plan?]
            if 'reset_location' in context and context['reset_location'] != '':
                context['place_a'] = location
                result += u'reset the depart from: %s\n' % location
            else:
                place_a = context['place_a']
                place_b = context['place_b']
                result += u'您目前的打车路线:\n%s,\n重置请按【0】。' % str_from_to(place_a, place_b)
                context['reset_location'] = 'yes'
        else:
            # a plan is set
            context['place_b'] = location
            a, b = context['place_a'],context['place_b']
            rr = get_paths(a, b)
            result = get_dache_result_str(a, b, rr, security_message)
            rduration = get_rduration(rr)
            context['rduration'] = rduration

            # 计算相似路径
            trace = get_direction(a, b)
            name_list = get_similar_names(name, trace)
            for e in name_list:
                name_1 = e[0]
                if name_1 == name:
                    continue
                context_1 = kvstore_module.get_Context(name_1)
                a, b = context_1['place_a'], context_1['place_b']
                result += '\nsimilar: %s from 【%s】 to 【%s】' % (str(name_1), str(a), str(b))
    else:
        # set the start place
        context['place_a'] = location
        result += u'目前【出发地点】: %s!\n请分享下目的地吧!' % location

    kvstore_module.set_Context(name, context)
    weixin.sendMsg(name, result)

def deal_reset(weixin, name, value, context):
    if 'place_a' in context:
        context.pop('place_a')
    if 'place_b' in context:
        context.pop('place_b')
    if 'status' in context:
        context.pop('status')
    result = u'重置成功! 请重新分享起【出发地点】:'
    kvstore_module.set_Context(name, context)
    weixin.sendMsg(name, result)

def get_dache_result_str(a, b, rr, security_message):
    result = ''
    # result += u'赞!打车路线为:\n从 %s 到 %s\n以下是比价结果:\n%s\n重置请按【0】\n%s。' % (a, b, r, security_message)
    res = ''
    for item in rr:
        rname = item['name']
        rduration = item['duration']
        rdistance = item['distance']
        rs_price = item['single_price']
        rp_price = item['pool_price']
        rwait_time = item['wait_time']

        res +='-----------------------------------\r\n'
        res += '|app | price | pool | wait time(分钟)|\r\n'
        res += u'|' + dache_name[str(rname)] + '| ' + str(rs_price) + '元'
        res += ' | ' + str(rp_price) +  if rp_price > 0 else ''
        res += ' | ' + str(rwait_time / 60) + ' \n' if rwait_time > 0 else ''
        res += '\r\n'
    result += u'赞!打车路线为:\n从 %s 到 %s\n以下是比价结果:\n%s重置请按【0】\n%s。' % (a, b, res, security_message)
    return result

def deal_dache(weixin, name, value, context):
    result = ''
    if 'place_a' in context:
        if 'place_b' in context:
            # 成功打车
            a, b = context['place_a'],context['place_b']
            rr = get_paths(a, b)
            result = get_dache_result_str(a, b, rr, security_message)
            rduration = get_rduration(rr)
            context['rduration'] = rduration

            # 计算相似路径
            trace = get_direction(a, b)
            name_list = get_similar_names(name, trace)
            for e in name_list:
                name_1 = e[0]
                if name_1 == name:
                    continue
                context_1 = kvstore_module.get_Context(name_1)
                a, b = context_1['place_a'], context_1['place_b']
                result += '\nsimilar: %s from 【%s】 to 【%s】' % (str(name_1), str(a), str(b))
        else:
            result += u'亲, 请分享下目的地, 我能帮你挑选最佳打车的app哟!\n'
    else:
        result += u'亲, 请分享一下出发地点把?\n'

    kvstore_module.set_Context(name, context)
    weixin.sendMsg(name, result)

def get_rduration(rr):
    rduration = 0
    for item in rr:
        if item['duration'] > 0:
            rduration = item['duration']
    return rduration

def deal_dengche(weixin, name, value, context):
    youxi = kvstore_module.get_youxi()
    result = '累了吧!玩个游戏把!\n' + youxi['content']
    weixin.sendMsg(name, result)


def deal_anquan(weixin, name, value, context):
    result = ''
    if not 'dingdan' in context:
        result += '建议分享您的打车订单, 便于在危险时刻分享给您的紧急联系人。\n如果安全抵达, 输入紧急联系人手机号后四位解除守护!'
    if not 'number' in context:
        result += '请输入一个紧急联系人手机号:'
    weixin.sendMsg(name, result)
    # afterdeal_anquan(weixin, name, value, context)

# def afterdeal_anquan(weixin, name, value, context):
#     result = ''
#     dt = datetime.now().timestamp()
#     result += '【亲爱哒，已经过去s% min时间了，输入您的【保护口令】，取消发送，否则过1分钟后巴迪将会发送短信给您的小伙伴】' %context['rduration']

# 设置紧急联系人, 解除安全守护
def deal_number(weixin, name, value, context):
    result = ''
    if len(value) == 11:
        context['number'] = value
        result = '【安全】已经为您启动安全守护模式! \n如需解除, 请输入紧急联系人手机号后四位!'
    elif len(value) == 4:
        if 'number' in context:
            if context['number'][-4,-1]==value:
                context.pop('number')
                result = '【安全】安全守护模式已解除!'
        else:
            result = '【安全】输入11位数字更改紧急联系人手机号!\n如需解除, 请输入紧急联系人手机号后四位!'

    kvstore_module.set_Context(name, context)
    weixin.sendMsg(name, result)


def deal_order(weixin, name, value, context):
    context['order'] = value
    # context['timeout'] = 2 * 60 * 60
    result = '【安全】订单已为您暂存!\n'
    if not 'number' in context:
        result += '【安全】还未设置紧急联系人! 请输入他的手机号:\n'
    result = '【如需解除守护模式, 请输入紧急联系人手机后四位!'

    kvstore_module.set_Context(name, context)
    weixin.sendMsg(name, result)


def deal_unknown(weixin, name, value, context):
    word = 'I dont understand!'
    weixin.sendMsg(name, word)


def str_from_to(place_a, place_b):
    return '(' + place_a + ') --> (' + place_b + ')'
