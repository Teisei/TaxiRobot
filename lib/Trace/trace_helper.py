#!/usr/bin/env python
# coding: utf-8
import operator

from Trace.rtree import node, Insert, merge
from kvstore_module import *
from factory import *
import math


def get_trace_by_name(name):
    context = get_Context(name)
    if not 'trace' in context:
        return None
    return context['trace']

# add nodes in the rtree,
# add node-trace to inverted index
def add_trace(name, trace):
    rtree = get_rtree()
    inverted_kv = get_inverted_kv()
    for hanode in trace:
        x = hanode['lng']
        y = hanode['lat']
        key = str(x) + '_' + str(y)

        user_list = inverted_kv.get(key)
        # check if the node exists
        if user_list == None:
        # if not key in inverted_kv:
            user_list = []
        # update inverted index
        user_list.append(name)
        set_inverted_kv(key, user_list)
        # update rtree
        data = {'xmin': x, 'xmax': x + 0.00001, 'ymin': y, 'ymax': y + 0.00001}
        new_node = node(MBR=data, index=key)
        Insert(rtree, new_node)


def delete_trace(name, trace):
    inverted_kv = get_inverted_kv()
    for hanode in trace:
        x = hanode['lng']
        y = hanode['lat']
        key = str(x) + '_' + str(y)

        new_user_list = []
        user_list = inverted_kv.get(key)
        # check if the node exists
        if not user_list:
            user_list = []
        for u in user_list:
            if not u == name:
                new_user_list.append(u)
        set_inverted_kv(key, new_user_list)

def get_similar_nodes(trace):
    node_list = []
    count = dict()
    rtree = get_rtree()
    for hanode in trace:
        x = hanode['lng']
        y = hanode['lat']
        key = str(x) + '_' + str(y)
        if not key in node_list:
            node_list.append(key)

        mydata = {'xmin': x, 'xmax': x + 0.00001, 'ymin': y, 'ymax': y + 0.00001}
        n = node(MBR=mydata, index='test')
        results = rtree.Search(merge(n.MBR, n.MBR))
        for n1 in results:
            if not n1 in node_list:
                node_list.append(n1)
    #         if n1 in count:
    #             count[n1] += 1
    #         else:
    #             count[n1] = 1
    # # rank the similar nodes
    # sortedd = sorted(count.iteritems(), key=operator.itemgetter(1), reverse=True)
    return node_list

def update_trace(name, new_trace):
    context = get_Context(name)
    if 'trace' in context:
        old_trace = context['trace']
        delete_trace(name, old_trace)
    context['trace'] = new_trace
    set_Context(name, context)
    add_trace(name, new_trace)

def get_similar_names(name, trace):

    update_trace(name, trace)

    node_list = get_similar_nodes(trace)
    count = dict()
    score = dict()
    inverted_kv = get_inverted_kv()
    for key in node_list:
        name_list = inverted_kv.get(key)
        for name in name_list:
            if name in count:
                count[name] += 1
            else:
                count[name] = 1
                # # rank the similar nodes
    for name2, num in count.items():
        context = get_Context(name2)
        if 'trace' not in context:
            continue
        trace2 = context['trace']
        score[name2] = get_score(trace, trace2, num)
    sortedd = sorted(score.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedd

def get_score(trace1, trace2, num):
    min_length = float(min(len(trace1), len(trace2)))
    score = float(num) / min_length * get_cos(trace1, trace2)
    return score


def cos_dist(a, b):
    if len(a) != len(b):
        return None
    part_up = 0.0
    a_sq = 0.0
    b_sq = 0.0
    for a1, b1 in zip(a,b):
        part_up += a1*b1
        a_sq += a1**2
        b_sq += b1**2
    part_down = math.sqrt(a_sq*b_sq)
    if part_down == 0.0:
        return None
    else:
        return part_up / part_down

def get_cos(trace1, trace2):
    #   "lat":
    v1x = trace1[-1]['lng'] - trace1[0]['lng']
    v1y = trace1[-1]['lat'] - trace1[0]['lat']
    v2x = trace2[-1]['lng'] - trace2[0]['lng']
    v2y = trace2[-1]['lat'] - trace2[0]['lat']
    v1 = (v1x, v1y)
    v2 = (v2x, v2y)
    return cos_dist(v1, v2)


# return if the two trace is similar
def is_same_way(trace1, trace2):
    pass

v1 = (1,1)
v2 = (-1,-1)
print cos_dist(v1, v2)