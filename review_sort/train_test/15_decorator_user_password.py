#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"

"""
带有参数的装饰器
"""


def new_func(func):
    def wrapper(username, password):
        if username == 'root' and password == '123456789':
            print('通过认证')
            print('开始执行附加功能')
            return func()
        else:
            print('用户名或密码错误')
            return

    return wrapper


def new_func_two(func):
    def wrapper(*parts):
        if parts:
            if parts[0] == 'root' and parts[1] == '123456789':
                return func()
        else:
            print('用户名或密码错误')
        return func()
    return wrapper


@new_func
def origin():
    print('开始执行函数')


@new_func_two
def origin_two():
    print('开始执行函数2')


origin('root', '12345678910')

origin_two('root', '12345678910')
