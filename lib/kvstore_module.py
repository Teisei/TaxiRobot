#!/usr/bin/env python
# coding: utf-8
import os
from solnlib.modular_input.checkpointer import FileCheckpointer

def get_file_checkpointer(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
    checkpointer = FileCheckpointer(dir)
    return checkpointer


# initial kv helper
user_path = os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'kv_store'), 'user')
topic_path = os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'kv_store'), 'topic')

user_helper = get_file_checkpointer(user_path)
topic_helper = get_file_checkpointer(topic_path)



def initiate_kv_helper():
    user_helper = get_file_checkpointer(user_path)
    topic_helper = get_file_checkpointer(topic_path)


def get_Context(name):
    if user_helper == None:
        initiate_kv_helper()
    context = user_helper.get(name)
    if context == None:
        context = {'test_key': 'test_value'}
    return context


def set_Context(name, context):
    if user_helper == None:
        initiate_kv_helper()
    user_helper.update(name, context)




