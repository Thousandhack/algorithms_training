#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"

"""
将字符串 "k:1 |k1:2|k2:3|k3:4"，处理成字典 {k:1,k1:2,...}
"""


def str_dict(str_demo):
    """
    #字典推导式 d = {k:int(v) for t in str1.split("|") for k, v in (t.split(":"), )}
    :param str_demo:
    :return:
    """
    dict_demo = {}
    for items in str_demo.split('|'):
        key, value = items.split(':')
        dict_demo[key] = value
    return dict_demo


if __name__ == "__main__":
    res = str_dict(str_demo="k:1|k1:2|k2:3|k3:4")
    print(res)
