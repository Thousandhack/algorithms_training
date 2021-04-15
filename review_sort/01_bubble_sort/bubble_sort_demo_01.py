#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"
"""
冒泡排序算法的工作原理如下：
    1.  比较相邻的元素。如果第一个比第二个大（升序），就交换他们两个。
    2.  对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
    3.  除了最后一个，所有的元素重复以上的步骤。
    4.  持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
"""


def bubble_sort(demo_list):
    # 外层循环控制比较几轮
    n = len(demo_list)
    for j in range(n - 1):
        # 内层循环控制交换
        # -j是不再换已经排好的
        for i in range(n - 1 - j):
            # 若前一个比后一个大，则换
            if demo_list[i] > demo_list[i + 1]:
                demo_list[i], demo_list[i + 1] = demo_list[i + 1], demo_list[i]


if __name__ == '__main__':
    demo_list = [33, 11, 26, 78, 3, 9, 40, -11]
    print("原来的列表：", demo_list)
    bubble_sort(demo_list)
    print("排序后的列表:", demo_list)
