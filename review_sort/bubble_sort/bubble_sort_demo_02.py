#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"


# 调优后的冒泡排序

def bubble_sort(alist):
    # 外层循环控制比较几轮
    n = len(alist)
    for j in range(n - 1):
        # 定义计数器
        count = 0
        # 内层循环控制交换
        # -j是不再换已经排好的
        for i in range(n - 1 - j):
            # 若前一个比后一个大，则换
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                # 计数器
                count += 1
        if count == 0:
            return


if __name__ == '__main__':
    li = [33, 11, 26, 78, 3, 9, 40]
    print("原来的列表：", li)
    bubble_sort(li)
    print("排序后的列表:", li)
