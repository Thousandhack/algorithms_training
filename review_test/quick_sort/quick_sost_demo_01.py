#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"
"""
快速排序使用分治法（Divide and conquer）策略来把一个串行（list）分为两个子串行（sub-lists）。
快速排序又是一种分而治之思想在排序算法上的典型应用。本质上来看，快速排序应该算是在冒泡排序基础上的递归分治法。

快速排序的名字起的是简单粗暴，因为一听到这个名字你就知道它存在的意义，就是快，而且效率高！它是处理大数据最快的排序算法之一了。

快速排序的最坏运行情况是 O(n²)，比如说顺序数列的快排。但它的平摊期望时间是 O(nlogn)，且 O(nlogn) 记号中隐含的常数因子很小，
比复杂度稳定等于 O(nlogn) 的归并排序要小很多。所以，对绝大多数顺序性较弱的随机数列而言，快速排序总是优于归并排序。

算法步骤:
1.从数列中挑出一个元素，称为 "基准"（pivot);

2.重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。
在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；

3.递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序；

"""


# 快排
# first理解为第一个位置的索引，last是最后位置索引
def quick_sort(list_demo, first, last):
    """

    :param list_demo:
    :param first:
    :param last:
    :return:
    """
    # 递归终止条件
    if first >= last:
        return

    # 设置第一个元素为中间值
    mid_value = list_demo[first]
    # low指向
    low = first
    # high
    high = last
    # 只要low小于high就一直走
    while low < high:
        # high大于中间值，则进入循环
        while low < high and list_demo[high] >= mid_value:
            # high往左走
            high -= 1
        # 出循环后，说明high小于中间值,low指向该值
        list_demo[low] = list_demo[high]
        # high走完了，让low走
        # low小于中间值，则进入循环
        while low < high and list_demo[low] < mid_value:
            # low向右走
            low += 1
        # 出循环后，说明low大于中间值,high指向该        8值
        list_demo[high] = list_demo[low]
    # 退出整个循环后，low和high相等
    # 将中间值放到中间位置
    list_demo[low] = mid_value
    # 递归
    # 先对左侧快排
    quick_sort(list_demo, first, low - 1)
    # 对右侧快排
    quick_sort(list_demo, low + 1, last)


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    quick_sort(li, 0, len(li) - 1)
    print(li)
