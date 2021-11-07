"""
13. 罗马数字转整数

罗马数字包含以下七种字符:I，V，X，L，C，D和M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做II，即为两个并列的 1。12 写做XII，即为X+II。 27 写做XXVII, 即为XX+V+II。

通常情况下，罗马数字中小的数字在大的数字的右边。
但也存在特例，例如 4 不写做IIII，而是IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。
同样地，数字 9 表示为IX。这个特殊的规则只适用于以下六种情况：

I可以放在V(5) 和X(10) 的左边，来表示 4 和 9。
X可以放在L(50) 和C(100) 的左边，来表示 40 和90。
C可以放在D(500) 和M(1000) 的左边，来表示400 和900。
给定一个罗马数字，将其转换成整数。输入确保在 1到 3999 的范围内。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/roman-to-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 法一：
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         dict_demo = {
#             "I": 1,
#             "V": 5,
#             "X": 10,
#             "L": 50,
#             "C": 100,
#             "D": 500,
#             "M": 1000
#         }
#         ret = 0
#         for index, value in enumerate(s):
#             """
#             如果还不是最后一位，并且后一位数得到的对应的整数大于前一位整数，那么就应该把要得到的结果减去这个数
#             """
#             if index < len(s) - 1 and dict_demo[s[index]] < dict_demo[s[index + 1]]:
#                 ret -= dict_demo[s[index]]
#             else:
#                 ret += dict_demo[s[index]]
#         return ret

# 法二：
class Solution:
    """
    从右到左遍历，记录当前遇到的最大的数字，遇到更大的就加，并且更新最大数，遇到小的就减
    例如：
    CLIV ==> VILC
    5 - 1 + 50 + 100
    """

    def romanToInt(self, s: str) -> int:
        dict_demo = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        high_num = 1
        ret = 0
        for v in s[::-1]:
            if dict_demo[v] >= high_num:
                ret += dict_demo[v]
                high_num = dict_demo[v]
            else:
                ret -= dict_demo[v]
        return ret


if __name__ == "__main__":
    print(Solution().romanToInt("CLIV"))
