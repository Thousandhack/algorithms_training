from typing import List


class Solution:
    """
    题目:有多少小于当前数字的数字
    给你一个数组 nums，对于其中每个元素 nums[i]，请你统计数组中比它小的所有数字的数目。
    换而言之，对于每个 nums[i] 你必须计算出有效的 j 的数量，其中 j 满足 j != i 且 nums[j] < nums[i] 。
    以数组形式返回答案。

    复制一个list，用原list和复制的list做循环对比
    两个for循环做对比,对外层循环的元素里面进行内循环,只有这个数超过的时候才说明元素的位置已经过去
    刚好进行记录
    """

    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        new_nums = nums
        res_list = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(new_nums)):
                if nums[i] > new_nums[j]:
                    count += 1
                else:
                    continue
            res_list.append(count)
        return res_list


if __name__ == "__main__":
    res = Solution().smallerNumbersThanCurrent([8, 1, 2, 2, 3])
    print(res)
