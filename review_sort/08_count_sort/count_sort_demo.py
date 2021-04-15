#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"

"""
计数排序是典型的空间换时间算法，开辟额外数据空间存储用索引号记录数组的值和数组值个数

算法描述：

找出待排序的数组的最大值和最小值
统计数组值的个数
反向填充目标数组

计数排序要求输入数据的范围在 [0,N-1] 之间，则可以开辟一个大小为 N 的数组空间，
将输入的数据值转化为键存储在该数组空间中，数组中的元素为该元素出现的个数。
它是一种线性时间复杂度的排序。

稳定排序，外排序，时间复杂度O(n + k)O(n+k)，但是对于数据范围很大的数组，需要大量时间和内存。
"""


def count_sort(nums):
    bucket = [0] * (max(nums) + 1)  # 桶的个数
    for num in nums:  # 将元素值作为键值存储在桶中，记录其出现的次数
        bucket[num] += 1
    i = 0  # nums 的索引
    for j in range(len(bucket)):
        while bucket[j] > 0:
            nums[i] = j
            bucket[j] -= 1
            i += 1
    return nums


if __name__ == '__main__':
    # li = [3, 11, 26, 26, 7, 3, 9, 4]
    li = [26, 54, 93, 17, 31, 44, 55, 20]
    print(li)
    result_list = count_sort(li)
    print(result_list)
