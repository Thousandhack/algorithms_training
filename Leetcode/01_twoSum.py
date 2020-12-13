from typing import List

"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        解题思路为:
            将所给列表都循环一遍,另外一个数一定为和减去第一个数
            如果 num not in dict_demo存在,就说明找到 i 的另外一个数和为target了
            一个数是通过字典找到位置,一个是通过循环的第几次找到位置
        :param nums:
        :param target:
        :return:
        """
        dict_demo = {}
        for i in range(0, len(nums)):
            num = target - nums[i]
            if num not in dict_demo:
                dict_demo[nums[i]] = i
            else:
                return [dict_demo[num], i]


if __name__ == "__main__":
    res = Solution().twoSum([2, 5, 5, 11], 10)
    print(res)
