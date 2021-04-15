#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"


def bubble_sort(list_demo):
    n = len(list_demo)
    for j in range(n - 1):
        count = 0
        for i in range(n - 1 - j):
            if list_demo[i] > list_demo[i + 1]:
                list_demo[i], list_demo[i + 1] = list_demo[i + 1], list_demo[i]
                count += 1
        if count == 0:
            return


def select_sort(list_demo):
    n = len(list_demo)
    for j in range(n - 1):
        min_index = j
        for i in range(j + 1, n):
            if list_demo[min_index] > list_demo[i]:
                min_index = i
        # 如果j 有变化，就说明存在比j小的值
        if j != min_index:
            list_demo[j], list_demo[min_index] = list_demo[min_index], list_demo[j]


if __name__ == "__main__":
    demo = [8, 5, 6, 3]
    # bubble_sort(demo)
    select_sort(demo)
    print(demo)
