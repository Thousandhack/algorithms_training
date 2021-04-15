#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"


def find_second_large_num(num_list):
    """ 找出数组第2大的数字 """
    # 方法一 # 直接排序，输出倒数第二个数即可
    tmp_list = sorted(num_list)
    print("方法一\nSecond_large_num is :", tmp_list[-2])

    # 方法二 # 设置两个标志位一个存储最大数一个存储次大数 # two 存储次大值，
    # one 存储最大值，遍历一次数组即可，先判断是否大于 one，
    # 若大于将 one 的 值给 two，将 num_list[i] 的值给 one，
    # 否则比较是否大于two，若大于直接将 num_list[i] 的值给 two，否则pass

    one = num_list[0]
    two = num_list[0]
    for i in range(1, len(num_list)):
        if num_list[i] > one:
            two = one
            one = num_list[i]
        elif num_list[i] > two:
            two = num_list[i]
    print("方法二\nSecond_large_num is :", two)

    # 方法三
    # 用 reduce 与逻辑符号 (and, or)
    # 基本思路与方法二一样，但是不需要用 if 进行判断。
    from functools import reduce
    num = reduce(lambda ot, x: ot[1] < x and (ot[1], x) or ot[0] < x and (x, ot[1]) or ot, num_list, (0, 0))[0]
    print("方法三\nSecond_large_num is :", num)


if __name__ == '__main___':
    num_list = [34, 11, 23, 56, 78, 0, 9, 12, 3, 7, 5]
    find_second_large_num(num_list)
