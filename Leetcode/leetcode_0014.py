from typing import List

"""
14. 最长公共前缀
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1：
输入：strs = ["flower","flow","flight"]
输出："fl"
示例 2：
输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。


提示：
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] 仅由小写英文字母组成

"""

"""
法一：横向扫描
    依次遍历字符串数组中的每个字符串，对于每个遍历到的字符串，更新最长公共前缀，当遍历完所有的字符串以后，即可得到字符串中的最长字符串公共前缀
"""

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not strs:
#             return ""
#         # 第一个元素字符串设置为默认前缀
#         prefix = strs[0]
#         count = len(strs)
#         for i in range(1, count):
#             prefix = self.lcp(prefix, strs[i])
#             if not prefix:
#                 break
#         return prefix
#
#     def lcp(self, str1, str2):
#         """
#         对两个字符串的相同位置的元素进行比较是否相同
#         如果相同公共前缀长度加1
#         :param str1:
#         :param str2:
#         :return:
#         """
#         length, index = min(len(str1), len(str2)), 0    # 得到最大公共的长度
#         while index < length and str1[index] == str2[index]:
#             index += 1
#         return str1[:index]

"""
法二：纵向扫描
遍历所有字符串的每一列，比较相同列上的字符是否相同，如果相同则继续对下一列进行比较，如果不相同则当前列不再属于公共前缀，当前列之前的部分为最长公共前缀。
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        length = len(strs[0])
        count = len(strs)
        for i in range(length):
            c = strs[0][i]
            # 循环每个列表里面的字符串与的某一位元素与列表第一个字符串的某一位元素进行比较，
            # 如果存在不相同的情况就返回第一个字符串到这某一位之前的数据为公共前缀
            if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, count)):
                return strs[0][:i]
        return strs[0]


if __name__ == "__main__":
    print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
