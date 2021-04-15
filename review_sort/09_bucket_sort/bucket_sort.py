#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"
"""

桶排序（Bucket Sort）
桶排序是计数排序的升级版，原理是：输入数据服从均匀分布的，将数据分到有限数量的桶里，
每个桶再分别排序（有可能再使用别的算法或是以递归方式继续使用桶排序，此文编码采用递归方式）

算法描述：
人为设置一个桶的BucketSize，作为每个桶放置多少个不同数值（意思就是BucketSize = 5，
可以放5个不同数字比如[1, 2, 3,4,5]也可以放 100000个3，只是表示该桶能存几个不同的数值）
遍历待排序数据，并且把数据一个一个放到对应的桶里去
对每个不是桶进行排序，可以使用其他排序方法，也递归排序
不是空的桶里数据拼接起来

稳定排序，外排序，时间复杂度O(n + k)O(n+k)，k为桶的个数。
"""


def bucket_sort(nums, bucketSize):
    if len(nums) < 2:
        return nums
    _min = min(nums)
    _max = max(nums)
    # 需要桶个数
    bucketNum = (_max - _min) // bucketSize + 1
    buckets = [[] for _ in range(bucketNum)]
    for num in nums:
        # 放入相应的桶中
        buckets[(num - _min) // bucketSize].append(num)
    res = []

    for bucket in buckets:
        if not bucket: continue
        if bucketSize == 1:
            res.extend(bucket)
        else:
            # 当都装在一个桶里,说明桶容量大了
            if bucketNum == 1:
                bucketSize -= 1
            res.extend(bucket_sort(bucket, bucketSize))
    return res


if __name__ == '__main__':
    # li = [3, 11, 26, 26, 7, 3, 9, 4]
    li = [26, 54, 93, 17, 31, 44, 55, 20]
    print(li)
    result_list = bucket_sort(li, 5)
    print(result_list)
