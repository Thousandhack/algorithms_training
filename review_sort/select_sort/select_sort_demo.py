#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"

"""
选择排序算法的工作原理如下：
    1. 首先在序列中找到最小或最大元素，存放到排序序列的前或后。
    2. 然后，再从剩余元素中继续寻找最小或最大元素。
    3. 然后放到已排序序列的末尾。
    4. 以此类推，直到所有元素均排序完毕。
"""


def select_sort(demo_list):
    n = len(demo_list)
    # 外层控制比较几轮
    for j in range(n - 1):
        min_index = j
        # 内层控制元素比较和更新索引
        for i in range(j + 1, n):
            # 进行比较
            if demo_list[min_index] > demo_list[i]:  # 大于为正序  小于为倒序(小于为max_index)
                # 更新索引
                min_index = i
        # 退出循环后，交换数据
        demo_list[j], demo_list[min_index] = demo_list[min_index], demo_list[j]
    return demo_list


if __name__ == '__main__':
    # li = [3, 11, 26, 26, 7, 3, 9, 4]
    li = [26, 54, 93, 17, 31, 44, 55, 20]
    print(li)
    result_list = select_sort(li)
    print(result_list)
    # print(id(li[0]))
