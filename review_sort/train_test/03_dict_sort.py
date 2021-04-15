#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"

"""
现有字典 d= {'a':24,'g':52,'i':12,'k':33}请按value值进行排序?

"""

dict_demo = {'a': 24, 'g': 52, 'i': 12, 'k': 33}
# sorted 可以对所有可迭代的对象进行排序操作。
# x[0]代表用key进行排序；x[1]代表用value进行排序。

print(sorted(dict_demo.items(), key=lambda x: x[1]))

"""
请按alist中元素的age由大到小排序
reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。
"""
list_one = [{'name': 'a', 'age': 20}, {'name': 'b', 'age': 30}, {'name': 'c', 'age': 25}]


def sort_by_age(list_one):
    return sorted(list_one, key=lambda x: x['age'], reverse=True)


print(sort_by_age(list_one=list_one))
