#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"
"""
8.一行代码实现1-100之和
"""

count = sum(range(0, 101))
print(count)

num = 0
for i in range(0, 101):
    num += i

print(num)

"""
.用一行python代码写出1+2+3+10248
"""
from functools import reduce

# 1.使用sum内置求和函数
num = sum([1, 2, 3, 10248])
print(num)
# 2.reduce 函数
num_1 = reduce(lambda x, y: x + y, [1, 2, 3, 10248])
print(num_1)
