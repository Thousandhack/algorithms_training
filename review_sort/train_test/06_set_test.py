#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"

"""
给定两个列表，怎么找出他们相同的元素和不同的元素？
"""
list1 = [1, 2, 3]
list2 = [3, 4, 5]
set1 = set(list1)
set2 = set(list2)
print(set1 & set2)
print(set1 ^ set2)
