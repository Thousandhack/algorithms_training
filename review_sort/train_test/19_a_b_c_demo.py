#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"

"""
如果a + b + c = 1000,且 a2 + b2 = c2 （a,b,c为自然数），如何求出所有a,b,c可能的组合
"""

import time

# start_time = time.time()
#
# # 注意是三重循环
#
# for a in range(0, 1001):
#     for b in range(0, 1001):
#         for c in range(0, 1001):
#             if a + b + c == 1000 and a ^ 2 + b ^ 2 == c ^ 2:
#                 print("a,b,c:%d,%d,%d" % (a, b, c))
#
# end_time = time.time()
#
# print(end_time - start_time)
# print("complete")
start_time = time.time()
for a in range(0, 1001):
    for b in range(0, 1001 - a):
        c = 1000 - a - b
        if a ^ 2 + b ^ 2 == c ^ 2:
            if a + b + c == 1000 and a ^ 2 + b ^ 2 == c ^ 2:
                print("a,b,c:%d,%d,%d" % (a, b, c))

end_time = time.time()

print(end_time - start_time)
print("complete")
