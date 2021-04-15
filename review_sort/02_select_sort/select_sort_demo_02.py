#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"


def select_sort(list_demo):
    n = len(list_demo)
    for j in range(n - 1):
        min_index = j
        for i in range(j + 1, n):
            if list_demo[min_index] > list_demo[i]:
                min_index = i
        # j 不是最小数时，将 j 和最小数进行交换
        if j != min_index:
            list_demo[j], list_demo[min_index] = list_demo[min_index], list_demo[j]


if __name__ == "__main__":
    li = [7, 9, 3, 5, 1]
    print(li)
    select_sort(li)
    print(li)
