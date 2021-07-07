#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

"""
二分法是一种效率比较高的搜索方法，时间复杂度为 O(log2n) 。

使用二分法查询 确定一个元素在一个有序列表中的位置
"""


def binary_search(list_demo, item):
    """
    使用递归的思想
    返回是否存在列表中
    :param list_demo:
    :param item:
    :return:
    """
    if len(list_demo) == 0:
        return False
    else:
        mid = len(list_demo) // 2
        if item == list_demo[mid]:
            return True
        elif item < list_demo[mid]:
            return binary_search(list_demo[:mid], item)
        else:
            return binary_search(list_demo[mid + 1:], item)


def binary_search_two(list_demo, item):
    """
    返回元素的位置
    :param list_demo:
    :param item:
    :return:
    """
    first = 0  # 起始下标为0
    last = len(list_demo) - 1  # 列表最后一位的索引
    while first <= last:  # 列表中间位置的索引值
        mid = (first + last) // 2
        if item == list_demo[mid]:
            return mid
        elif item < list_demo[mid]:
            last = mid - 1
        else:
            first = mid + 1
    else:
        return False


if __name__ == "__main__":
    demo = [5, 10, 15, 18, 35, 55, 65, 75, 99, 200, 230, 340]  # 有序序列
    print(binary_search(demo, 200))
    print(binary_search_two(demo, 200))
