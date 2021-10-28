"""
7. 整数反转
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
如果反转后整数超过 32 位的有符号整数的范围[−2^31,2^31− 1] ，就返回 0。
假设环境不允许存储 64 位整数（有符号或无符号）。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer

示例 1：
输入：x = 123
输出：321

示例 2：
输入：x = -123
输出：-321
"""


class Solution:
    def reverse(self, x: int) -> int:
        if -2 ** 31 < x < 2 ** 31 - 1:
            if x >= 0:
                x = int(str(x)[::-1])
                if 0 < x < 2 ** 31 - 1:
                    return x
                else:
                    return 0
            else:
                x = - int(str(0 - x)[::-1])
                if -2 ** 31 < x < 0:
                    return x
                else:
                    return 0
        else:
            return 0


if __name__ == "__main__":
    print(Solution().reverse(-1563847412))
