# !/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz


"""
请实现cache 功能 ：若在n 秒内使用相同keywords调用 query 函数进行查询，则直接返回query函数
上一次返回的内容，否则需要调用get_news重新查询，请构造出命中和不命中cache以及cache 超时的场景，执行结果分别打印出请求是否使用缓存以及使用缓存的超时情况

"""
import time


def cache(the_time):
    def inner(func):
        cache_dict = {}

        def wrapper(*args):
            result = None
            if args[0] in cache_dict.keys():
                (result, updateTime) = cache_dict[args[0]]
                if time.time() - updateTime < the_time:
                    result = updateTime
                else:
                    result = None
            else:
                if result is None:
                    result = func(*args)
                    cache_dict[args[0]] = (result, time.time())
            return result

        return wrapper

    return inner


def get_news(keywords):
    print("query db get keywords data")
    # print(keywords)
    return {"keywords": "data for keywords"}


@cache(10)
def query(keywords):
    news = get_news(keywords)
    print(news, "111111111")


query("keywords")
query("keywords")
