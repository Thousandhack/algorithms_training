# !/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ hsz

"""
所谓“变位词”是指两个词之间存在组成字母的重新排列关系
"""

"""
解决方式一：逐字检查
解法思路
将词1 中的字符逐个到词2 中检查是否存在
存在就 “ 打勾 ” 标记（防止重复检查）
如果每个字符都能找到，则两个词是变位词，
只要有1个字符找不到，就不是变位词。
"""


def anagram_solution(str_one, str_two):
    if len(str_one) != len(str_two):
        return False
    list_two = list(str_two)
    pos_one = 0
    still = True
    while pos_one < len(str_one) and still:
        pos_two = 0
        found = False
        while pos_two < len(list_two) and not found:
            if str_one[pos_one] == list_two[pos_two]:
                found = True
            else:
                pos_two = pos_two + 1
        if found:
            list_two[pos_two] = None
        else:
            still = False
        pos_one = pos_one + 1
    return still


"""
解决方法二：排序比较
两个sort并不是无代价的
本算法的运行时间数量级就等于排序过程
的数量级O(n log n)
"""


def anagram_solution_two(str_one, str_two):
    if len(str_one) != len(str_two):
        return False
    list_one = list(str_one)
    list_one.sort()
    list_two = list(str_two)
    list_two.sort()
    pos = 0
    still = True
    while pos < len(str_one) and still:
        if list_one[pos] == list_two[pos]:
            pos += 1
        else:
            still = False

    return still


"""
解法4：计数比较-算法分析
❖解题思路：对比两个词中每个字母出现的
次数，如果26个字母出现的次数都相同的
话，这两个字符串就一定是变位词
❖具体做法：为每个词设置一个26位的计数
器，先检查每个词，在计数器中设定好每
个字母出现的次数
❖计数完成后，进入比较阶段，看两个字符
串的计数器是否相同，如果相同则输出是
变位词的结论


值得注意的是，本算法依赖于两个长度为
26的计数器列表，来保存字符计数，这相
比前3个算法需要更多的存储空间
如果考虑由大字符集构成的词（如中文具有上万
不同字符），还会需要更多存储空间。
"""


def anagram_solution_three(str_one, str_two):
    if len(str_one) != len(str_two):
        return False
    list_one = [0] * 26
    list_two = [0] * 26
    for i in range(len(str_one)):
        pos = ord(str_one[i]) - ord('a')
        list_one[pos] = list_one[pos] + 1

    for i in range(len(str_two)):
        pos = ord(str_two[i]) - ord('a')
        list_two[pos] = list_two[pos] + 1
    j = 0
    still = True
    while j < 26 and still:
        if list_one[j] == list_two[j]:
            j += 1
        else:
            still = False
    return still


if __name__ == "__main__":
    print("=========法一=======================================")
    print(anagram_solution('abcd32', 'acbd32'))
    print(anagram_solution('abcd322', 'acbd323'))
    print("=========法二=======================================")
    print(anagram_solution_two('abcd32', 'acbd32'))
    print(anagram_solution_two('abcd322', 'acbd323'))
    print("=========法三=======条件仅限于小写字母==============")
    print(anagram_solution_three('abcdgd', 'acbdgd'))
    print(anagram_solution_three('abcdhz', 'acbdha'))
