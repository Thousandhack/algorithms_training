#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "hsz"

import atexit

"""
在进程退出的时候运行一些函数
使用atexit.register

"""


# 方法一：
# def f(s):
#     print(s)
#
#
# atexit.register(f, "hello")


# 方法二：

# @atexit.register
# def func_demo():
#     print("========")
#
#
# # 将本来要退出进程注册进来的函数，又取消注册，也就是就不运行了
# atexit.unregister(func_demo)

# 同一个函数注册多次，只需要取消注册一次就可以了。

class MyClass:
    def __call__(self):
        print("exiting")

    def __eq__(self, other):
        if isinstance(other, MyClass):
            return True
        return False


    # 官方文档说的是is 不是 == ,所以也是介意到达取消注册的效果


f0 = MyClass()
atexit.register(f0)
# f1 = MyClass()
# atexit.unregister(f1)

# 不管python程序正常结束还是异常退出，这个函数如果被atexit.register了都可以运行

# 有一种情况会导致atexit.register不会运行就是 os._exit(0)
# 因为os._exit(0)是系统的东西导致python程序没有办法按照自己的正常流程运行


