def two_sum(nums, target):
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