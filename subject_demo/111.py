#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
from functools import wraps


def cache(func):
    saved = {}

    @wraps(func)
    def newfunc(*args):
        if args in saved:
            return newfunc(*args)  # should be return saved[args]?
        result = func(*args)
        saved[args] = result
        return result

    return newfunc


def get_news(keywords):
    print("query db get keywords data")
    # print(keywords)
    return {"keywords": "data for keywords"}


@cache  #(10)
def query(keywords):
    news = get_news(keywords)
    print(news, "111111111")


query("keywords")
query("keywords")
