#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"

"""
堆排序是利用堆这个数据结构设计的排序算法。

算法描述：
建堆，从底向上调整堆，使得父亲节点比孩子节点值大，构成大顶堆；
交换堆顶和最后一个元素，重新调整堆。
调整堆方法写了递归和迭代，都很好理解！

"""


def heap_sort(nums):
    # 调整堆
    # 迭代写法
    # def adjust_heap(nums, startpos, endpos):
    #     newitem = nums[startpos]
    #     pos = startpos
    #     childpos = pos * 2 + 1
    #     while childpos < endpos:
    #         rightpos = childpos + 1
    #         if rightpos < endpos and nums[rightpos] >= nums[childpos]:
    #             childpos = rightpos
    #         if newitem < nums[childpos]:
    #             nums[pos] = nums[childpos]
    #             pos = childpos
    #             childpos = pos * 2 + 1
    #         else:
    #             break
    #     nums[pos] = newitem

    # 递归写法
    def adjust_heap(nums, startpos, endpos):
        pos = startpos
        chilidpos = pos * 2 + 1
        if chilidpos < endpos:
            rightpos = chilidpos + 1
            if rightpos < endpos and nums[rightpos] > nums[chilidpos]:
                chilidpos = rightpos
            if nums[chilidpos] > nums[pos]:
                nums[pos], nums[chilidpos] = nums[chilidpos], nums[pos]
                adjust_heap(nums, pos, endpos)

    n = len(nums)
    # 建堆
    for i in reversed(range(n // 2)):
        adjust_heap(nums, i, n)
    # 调整堆
    for i in range(n - 1, -1, -1):
        nums[0], nums[i] = nums[i], nums[0]
        adjust_heap(nums, 0, i)
    return nums


if __name__ == '__main__':
    # li = [3, 11, 26, 26, 7, 3, 9, 4]
    li = [26, 54, 93, 17, 31, 44, 55, 20]
    print(li)
    result_list = heap_sort(li)
    print(result_list)

