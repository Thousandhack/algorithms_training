#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"

"""
归并排序（Merge sort）是建立在归并操作上的一种有效的排序算法。该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。
作为一种典型的分而治之思想的算法应用，归并排序的实现由两种方法：
    自上而下的递归（所有递归的方法都可以用迭代重写，所以就有了第 2 种方法）；
    自下而上的迭代；
步骤：
    申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列；
    设定两个指针，最初位置分别为两个已经排序序列的起始位置；
    比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置；
    重复步骤 3 直到某一指针达到序列尾；
    将另一序列剩下的所有元素直接复制到合并序列尾。
# 分治发的典型应用，大问题拆分成小问题，逐个击破，之后将结果合并
"""
import math


def merge_sort(list_demo):
    if len(list_demo) < 2:
        return list_demo
    middle = math.floor(len(list_demo) / 2)
    left, right = list_demo[0:middle], list_demo[middle:]
    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result


if __name__ == "__main__":
    li = [1, 7, 9, 5, 3]
    print(li)
    merge_sort(li)
    print(li)
