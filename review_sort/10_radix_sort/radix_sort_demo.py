#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"

"""
基数排序是对数字每一位进行排序，从最低位开始排序

算法描述：
找到数组最大值，得最大位数；
从最低位开始取每个位组成radix数组；
对radix进行计数排序（计数排序适用于小范围的特点）。

稳定排序，外排序，时间复杂度 posCount * (n + n)posCount∗(n+n) ，
其中 posCount 为数组中最大元素的最高位数；简化下得：$O( k *n ) $；其中k为常数，n为元素个数。


"""


def radix_sort(nums):
    if not nums: return []
    _max = max(nums)
    # 最大位数
    max_digit = len(str(_max))
    bucket_list = [[] for _ in range(10)]
    # 从低位开始排序
    div, mod = 1, 10
    for i in range(max_digit):
        for num in nums:
            bucket_list[num % mod // div].append(num)
        div *= 10
        mod *= 10
        idx = 0
        for j in range(10):
            for item in bucket_list[j]:
                nums[idx] = item
                idx += 1
            bucket_list[j] = []
    return nums


if __name__ == '__main__':
    # li = [3, 11, 26, 26, 7, 3, 9, 4]
    li = [26, 54, 93, 17, 31, 44, 55, 20]
    print(li)
    result_list = radix_sort(li)
    print(result_list)
