# -*- coding:utf-8 -*-

"""
20. 有效的括号
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
 

示例 1：
输入：s = "()"
输出：true

示例 2：
输入：s = "()[]{}"
输出：true

示例 3：
输入：s = "(]"
输出：false

示例 4：
输入：s = "([)]"
输出：false

示例 5：
输入：s = "{[]}"
输出：true
 

提示：
1 <= s.length <= 104
s 仅由括号 '()[]{}' 组成

"""

"""
法一：横向扫描
    依次遍历字符串数组中的每个字符串，对于每个遍历到的字符串，更新最长公共前缀，当遍历完所有的字符串以后，即可得到字符串中的最长字符串公共前缀
"""


class Solution:
    def isValid(self, s: str) -> bool:
        pass


if __name__ == "__main__":
    print(Solution().isValid("()"))
