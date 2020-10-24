# -*- coding:utf-8 -*-
"""
二维数组中的查找
题目： 在一个二维数组中（每个一维数组的长度相同），
每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

**思路：**遍历每一行，查找该元素是否在该行之中。
"""


class Solution:
    # array 二维列表
    def find_include(self, target, array):
        """
        双层循环遍历,一个个列表进行遍历判断是否存在这个元素
        :param target:
        :param array:
        :return:
        """
        for line in array:
            if target in line:
                return True
        return False


if __name__ == '__main__':
    target = 2
    array = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]]
    solution = Solution()
    res = solution.find_include(target, array)
    print(res)
