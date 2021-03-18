"""
题目描述
写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于5,向上取整；小于5，则向下取整。

"""
# 法一
num = float(input())
print(int(num) + 1 if num - int(num) >= 0.5 else int(num))

# 法二
num = float(input())
if num * 10 % 10 >= 5:
    print(int(num) + 1)
else:
    print(int(num))
