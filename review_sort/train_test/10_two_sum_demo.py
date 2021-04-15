#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"

"""
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。你可以假设每个输入只对应一种答
案，且同样的元素不能被重复利用。示例:给定nums = [2,7,11,15],target=9 因为 nums[0]+nums[1] =
2+7 =9,所以返回[0,1]
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int] """
        d = {}
        size = 0
        while size < len(nums):
            if target - nums[size] in d:
                if d[target - nums[size]] < size:
                    return [d[target - nums[size]], size]
                else:
                    d[nums[size]] = size
                size = size + 1
        return [d, size]


solution = Solution()
list = [2, 7, 11, 15]
target = 9
nums = solution.twoSum(list, target)
print(nums)
