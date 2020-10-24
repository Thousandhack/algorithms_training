"""
替换空格
题目： 请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

**思路：**利用字符串中的replace直接替换即可。
上面的思路就是将空格替换成%20 的字符串
"""


class Solution:
    def blank_repalce(self, demo_str: str):
        res = demo_str.replace(" ", "%20")

        return res


if __name__ == "__main__":
    demo_str = "We Are Happy"
    new_str = Solution().blank_repalce(demo_str)
    print(new_str)
