#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"

"""
栈的特点是 后进先出，先进后出
"""


class Stack(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    s = Stack()  # 创建一个空栈
    print(s.is_empty())  # 是空栈
    # 入栈
    s.push(4)
    s.push(3)
    s.push(8)
    print(s.items)  # 打印现在的栈
    print(s.size())
    s.pop()

    print(s.items)

    s.peek()
    print(s.items)
