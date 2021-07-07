#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

"""
计算两个非负整数的最大公约数
"""


def greatest(p, q):
    if q == 0:
        return p
    r = p % q
    return greatest(q, r)


if __name__ == "__main__":
    print(greatest(18, 9))
