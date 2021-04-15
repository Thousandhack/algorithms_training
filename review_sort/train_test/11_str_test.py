#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"

"""
给定一个任意长度数组，实现一个函数
让所有奇数都在偶数前面，而且奇数升序排列，偶数降序排序，如字符串'1982376455',变 成'1355798642
"""


# 方法一
def func1(l):
    if isinstance(l, str):
        num_list = [int(i) for i in l]
        num_list.sort(reverse=True)  # 降序排序

        for i in range(len(l)):
            if num_list[i] % 2 > 0:
                # print(num_list)
                num_list.insert(0, num_list.pop(i))
        print(''.join(str(e) for e in num_list))


func1('1982376455')


# 方法二
def func2(l):
    print("".join(sorted(l, key=lambda x: int(x) % 2 == 0 and 20 - int(x) or int(x))))


func2('1982376455')
