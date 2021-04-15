#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"

"""
装饰器实现简易限制函数调用频率，如10秒一次

"""

import math
import time

cache_dict = {}


def outer(n):
    def time_wrapper(func):
        start_time = 0
        print(n)

        def inner(*args, **kwargs):
            nonlocal start_time
            t = time.time() - start_time
            if t >= n:
                start_time = time.time()
                ret = func(*args, **kwargs)
                print("返回重新查询一次的结果")
                return ret
            else:
                print(f"还在冷却当中，倒计时{math.ceil(n - t)}秒")
                print("返回内存中的数据")
                if args not in cache_dict:
                    cache_dict[args] = func(*args)
                return cache_dict[args]

        return inner

    return time_wrapper


def get_news(key_words):
    print("来get news查询数据了")
    return {key_words: "query data key_words"}


@outer(5)
def test(key_words):
    print("运行了测试函数")
    return key_words
    # print("key_words:", key_words)


if __name__ == "__main__":
    res = test("hsz")
    print(res)
    time.sleep(4)

    ret = test("hsz")
    print(ret)
