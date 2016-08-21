#!/usr/bin/env python
# coding: utf-8

from unittest import TestCase
from kvstore_module import *

import sys
reload(sys)
sys.setdefaultencoding('utf8')

class TestKVStore(TestCase):

    def test_user_kv(self):
        name = 'teisei'
        context = get_Context(name)
        print context

    def test_set_user_kv(self):
        name = 'teisei'
        context = {
            "name":"teisei",
            "from_i": "11.11",
            "from_j": "22.22",
            "to_i": "33.33",
            "to_j": "44.44",
            "predict_time": 90,
            "contact": "18516216459",
            "password": 123456,
            "dingdan_info": {},
            "topic": ["game", "music"]
        }
        print get_Context(name)
        set_Context(name, context)
        print get_Context(name)

    def test_set_fun(self):
        add_xiaohua(1, '上学时和同学一起去打热水，回宿舍路上暖瓶吱吱的响。我说：“不好要炸啦。”这哥们嗖的一声把暖瓶扔出去了，嘭，果然炸了。这哥们心有余悸的说：“还好我扔的快，没炸到我。”')
        add_xiaohua(2, '经理追求女秘书。“亲爱的，你不是答应嫁给我吗？”“我在哪里说过这话？”“飞机上。”“哦，空话你也信?”')
        add_xiaohua(3, '孙子一手摸着爷爷的光头一手捋着爷爷的胡子说：“爷爷，人一变老，是不是头发都转移到下巴上了呢？”')
        add_xiaohua(4, '晚上与一朋友吃饭，喝高兴了，朋友突然对我说：“两个大老爷们吃没有意思，叫两女人来一起喝。”作为单身狗的我满怀期待的等着，最后来的竟然是她老婆和女儿。。。')

        add_xingzuo(1, '巴迪掐指一算，今日白羊座的运势最好，出门有桃花运呦')
        add_xingzuo(2, '白羊座有一种让人看见就觉得开心的感觉，因为总是看起来都是那么地热情、阳光、乐观、坚强，对朋友也慷概大方，性格直来直往，就是有点小脾气。白羊男有大男人主义的性格，而白羊女就是女汉子的形象。')
        add_xingzuo(3, '进入8月份，天秤座周遭的变故增多，无论是职场方面还是在婚姻方面，你都必须提前做好应对方案，各方面的决定应当思虑周全。提升自我的时候应当找准方向，最好不要病急乱投医。情侣可能不得不因为出国、求职、求学而分离。')
        add_xingzuo(4, '对于射手来说，2016年绝对不是一个好光景。最主要的原因是厄星进入了射手的对宫座，今年所发生的变化，射手都容易被波及。比如说事业上的沟通阻碍，爱情方面的小三上位，财运方面的人际折损等等。所以，最重要的还是保持好身心康泰，维稳为主，平安是福。')
        add_xingzuo(5, '2016年，金牛座工作和生活捷报频传，潜力无限，偶尔有逆转剧情出现，稍有不慎，将功亏一篑。')

        add_youxi(1, '微信小游戏：（链接）一毛钱不剩：https://dongxi.douban.com/special/caprice?bid=3xFv4sziE4&channel=zhihu')
        add_youxi(2, '切水果：http://g.huceo.com/weixin/qiexigua/index.html')
        add_youxi(3, '财务包子铺：http://baozipu.zhihu.com/?utm_campaign=game002&utm_source=zhihu&utm_medium=column&utm_content=gamepage')
        add_youxi(4, '见缝插针：http://g.huceo.com/weixin/chazhen/')
        add_youxi(5, '辨色大比拼：http://g.huceo.com/weixin/bianse/index.html')

    def test_get_fun(self):
        print get_xiaohua()
        print get_xingzuo()
        print get_youxi()


