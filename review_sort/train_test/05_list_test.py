#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"

"""
写一个列表生成式，产生一个公差为11的等差数列
"""
print([x * 11 for x in range(10)])

"""
请写出一段python代码实现删除list里面的重复元素？
"""
l1 = ['b', 'c', 'd', 'c', 'a', 'a']
l2 = list(set(l1))
print(l2)

l1 = ['b', 'c', 'd', 'c', 'a', 'a']
l2 = []
for i in l1:
    if not i in l2:
        l2.append(i)
print(l2)

print("=======================================")
"""
请写出一个函数满足以下条件
该函数的输入是一个仅包含数字的list,输出一个新的list，其中每一个元素要满足以下条件：
1、该元素是偶数
2、该元素在原list中是在偶数的位置(index是偶数)

"""


def num_list(num_demo):
    return [i for i in num_demo if i % 2 == 0 and num_demo.index(i) % 2 == 0]


num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

ret = num_list(num)

print(ret)

print("=======================================")
"""
使用单一的列表生成式来产生一个新的列表
该列表只包含满足以下条件的值，元素为原始列表中偶数切片
"""
list_data = [1, 2, 5, 8, 10, 3, 18, 6, 20]
res = [x for x in list_data[::2] if x % 2 == 0]

print(res)
print("=======================================")
"""
用一行代码生成[1,4,9,16,25,36,49,64,81,100]
"""
print([x * x for x in range(1,11)])
