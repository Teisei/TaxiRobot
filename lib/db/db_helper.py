#!/usr/bin/env python
# coding: utf-8
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
user_path = os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'kv_store'), 'user')
topic_path = os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'kv_store'), 'topic')


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

def add_xiaohua(id, content):
    xiaohua_list = topic_helper.get('xiaohua')
    if not xiaohua_list:
        xiaohua_list = []
    for xiaohua in xiaohua_list:
        if xiaohua['id'] == id:
            return
    xiaohua = {}
    xiaohua['id'] = id
    xiaohua['content'] = content
    xiaohua_list.append(xiaohua)
    topic_helper.update('xiaohua', xiaohua_list)

def add_xingzuo(id, content):
    xingzuo_list = topic_helper.get('xingzuo')
    if not xingzuo_list:
        xingzuo_list = []
    for xingzuo in xingzuo_list:
        if xingzuo['id'] == id:
            return
    xingzuo = {}
    xingzuo['id'] = id
    xingzuo['content'] = content
    xingzuo_list.append(xingzuo)
    topic_helper.update('xingzuo', xingzuo_list)

def add_youxi(id, content):
    youxi_list = topic_helper.get('youxi')
    if not youxi_list:
        youxi_list = []
    for youxi in youxi_list:
        if youxi['id'] == id:
            return
    youxi = {}
    youxi['id'] = id
    youxi['content'] = content
    youxi_list.append(youxi)
    topic_helper.update('youxi', youxi_list)

def get_xiaohua():
    xiaohua_list = topic_helper.get('xiaohua')
    return xiaohua_list[0]

def get_xingzuo():
    xingzuo_list = topic_helper.get('xingzuo')
    return xingzuo_list[0]

def get_youxi():
    youxi_list = topic_helper.get('youxi')
    return youxi_list[0]

