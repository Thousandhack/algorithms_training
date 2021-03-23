#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"


# 归并排序，还有些问题。其中有些细节需要重新理解
# 也是递归问题


def merge_sort(data):  # 分治发的典型应用，大问题拆分成小问题，逐个击破，之后将结果合并
    half_index = int(len(data) / 2)  # 将数组拆分

    right = data[:half_index]
    left = data[half_index:]

    if len(right) > 1:
        right = merge_sort(right)

    if len(left) > 1:
        left = merge_sort(left)

    index = 0
    for i in range(len(left)):
        state = 1
        for j in range(index, len(right)):
            if left[i] < right[j]:
                state = 0
                index = j + 1
                right.insert(j, left[i])
                break
        if state == 1:  # 如果大于d0这个队列的所有值，那么直接extend所有数据
            right.extend(left[i:])
            break
    return right


if __name__ == "__main__":
    d0_in = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]  # 原始乱序
    d0_out = [2, 2, 2, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 9, 12, 15, 44, 45, 54, 64]  # 正确排序
    d1_out = merge_sort(d0_in)
    print(d1_out)
    print(d0_out)
