#!/usr/bin/env python
# coding: utf-8
import os
#设置一个根节点，m=3，M=7
from Trace.rtree import Rtree
from solnlib.modular_input import FileCheckpointer


def get_file_checkpointer(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
    checkpointer = FileCheckpointer(dir)
    return checkpointer

rtree = Rtree(m = 3, M = 7)

def get_rtree():
    global rtree
    if rtree == None:
        rtree = Rtree(m = 3, M = 7)
    return rtree

# initial kv helper
user_path = os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'kv_store'), 'user')
topic_path = os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'kv_store'), 'topic')
inverted_path = os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'kv_store'), 'inverted')

user_kv = get_file_checkpointer(user_path)
topic_kv = get_file_checkpointer(topic_path)
inverted_kv = get_file_checkpointer(inverted_path)

def get_user_kv():
    global user_kv
    if user_kv == None:
        user_kv = get_file_checkpointer(user_path)
    return user_kv

def get_topic_kv():
    global topic_kv
    if topic_kv == None:
        topic_kv = get_file_checkpointer(topic_path)
    return topic_kv

def get_inverted_kv():
    global inverted_kv
    if inverted_kv == None:
        inverted_kv = get_file_checkpointer(inverted_path)
    return inverted_kv

def set_inverted_kv(key, value):
    inverted_kv.update(key, value)