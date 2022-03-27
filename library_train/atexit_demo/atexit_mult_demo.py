#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "hsz"

import atexit
import multiprocessing


def t():
    def f():
        print("exiting")
        atexit.register(f)


p = multiprocessing.Process(target=t)
p.start()
p.join()
