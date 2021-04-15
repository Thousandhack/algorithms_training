#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"

"""
1
121
1331
14641
15101051
杨辉三角 - 二项式的n次方展开系数
"""


def test(num):
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()


test(5)

"""
利用zip()和sum()这两个方法
"""


def generate_two(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    l1 = [1]
    l2 = []
    n = 0
    while n < numRows:
        l2.append(l1)
        l1 = [sum(t) for t in zip([0] + l1, l1 + [0])]
        n += 1
    return l2


res = generate_two(6)
print(res)


def generate_three(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    if numRows == 0:
        return []
    l1 = [[1]]
    n = 1
    while n < numRows:
        l1.append(map(lambda x, y: x + y, [0] + l1[-1], l1[-1] + [0]))
        n += 1
    return l1


res = generate_three(6)
print(res)
