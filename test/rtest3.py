#!/usr/bin/python
# -*- coding: utf-8 -*-
from time import time

from Trace.rtree import *

data = {}


mylist = [{
		"lng": 116.33939925532,
		"lat": 40.002301881948
	},{
		"lng": 116.33939935532,
		"lat": 40.002301884948
	}, {
		"lng": 116.33939925532,
		"lat": 40.0023919023
	}, {
		"lng": 116.33920926371,
		"lat": 40.000733380731
	}, {
		"lng": 116.33932999597,
		"lat": 39.998552700912
	}, {
		"lng": 116.3285390112,
		"lat": 39.998332162518
	}
]

mynode = {
		"lng": 116.33939925531,
		"lat": 40.002301881942
}

#初始化10000个坐标在(-1000, 1000)间，面积为0.01的矩形。
inx = 0
for hanode in mylist:
    x = hanode['lng']
    y = hanode['lat']
    data[inx] = {'xmin':x, 'xmax':x + 0.00001, 'ymin':y, 'ymax':y + 0.00001}
    inx += 1

#设置一个根节点，m=3，M=7
root = Rtree(m = 3, M = 7)
n = []

for i in range(0, inx):
    hanode = node(MBR = data[i], index = str(i))
    n.append(hanode)
    print i
t0 = time()

#插入
for i in range(0, inx):
    Insert(root, n[i])
t1 = time()
print 'Inserting ...'
print t1 - t0



#搜索
print '\n\nsearch...'
x = mynode['lng']
y = mynode['lat']
mydata = {'xmin':x, 'xmax':x + 0.00001, 'ymin':y, 'ymax':y + 0.00001}
hanode = node(MBR = mydata, index = 1000)
x = root.Search(merge(hanode.MBR, hanode.MBR))
print x
t2 = time()
# print 'Searching ...'
# print t2 - t1

#删除
for i in range(0, inx):
    root = Delete(root, n[i])
t3 = time()
print 'Deleting ...'
print t3 - t2




