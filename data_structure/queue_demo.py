#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"

"""
队列的特点是先进先出
"""


class Queue(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def en_queue(self, item):
        self.items.insert(0, item)

    def de_queue(self):
        del self.items[0]


if __name__ == "__main__":
    q = Queue()  # 创建一个队列
    print(q.is_empty())  # 是空栈
    # 入队
    q.en_queue(4)
    q.en_queue(3)
    q.en_queue(8)
    print(q.items)
    # 出队
    q.de_queue()
    q.de_queue()
    print(q.items)
