# -*- coding:utf-8 -*-

"""
9. 回文数
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。


示例 1：
输入：x = 121
输出：true
示例 2：

输入：x = -121
输出：false
解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

示例 3：
输入：x = 10
输出：false
解释：从右向左读, 为 01 。因此它不是一个回文数

示例 4：
输入：x = -101
输出：false


提示：
-231 <= x <= 231 - 1

进阶：你能不将整数转为字符串来解决这个问题吗？
"""


# 法一：将数字对半分开，前半部分和后半部分相同即可
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False
#         y = str(x)
#         x_length = len(y)
#         if x_length % 2 == 0:
#             half_length = int(x_length / 2)
#             if y[:half_length][::-1] == y[half_length:]:
#                 return True
#             else:
#                 return False
#         else:
#             half_length = int((x_length - 1) / 2)
#             if y[:half_length][::-1] == y[half_length + 1:]:
#                 return True
#             else:
#                 return False


# 少代码版本
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False
#         y = str(x)
#         l = len(y)
#         h = int(l/2)
#         return y[:h] == y[-1:-h-1:-1]


# 方法二：将一个数变成字符串进行遍历，第一个数和最后一个数相同用字符串方式切割进行比较是否相等，全部相等就是回文数
class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        l = len(y)
        for i in range(0, int((l + 1) / 2)):
            # 将这个
            if y[i:i + 1] != y[l - i - 1:l - i]:
                return False
        return True


if __name__ == "__main__":
    print(Solution().isPalindrome(11))
