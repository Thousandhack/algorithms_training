#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"

"""
Python-遍历列表时删除元素的正确做法
遍历在新在列表操作，删除时在原来的列表操作
"""

a = [1, 2, 3, 4, 5, 6, 7, 8]
print(id(a))
print(id(a[:]))
for i in a[:]:
    if i > 5:
        pass
    else:
        a.remove(i)
    print(a)
print('-----------')
print(id(a))
print('-----------')
# filter
a = [1, 2, 3, 4, 5, 6, 7, 8]
b = filter(lambda x: x > 5, a)
print(list(b))

print('-----------')
a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [i for i in a if i > 5]
print(b)
