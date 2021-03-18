"""
题目描述
输入一个int型的正整数，计算出该int型数据在内存中存储时1的个数。

"""
# 法一
n = int(input())
n = bin(n)
print(n.count('1'))

# 法二
