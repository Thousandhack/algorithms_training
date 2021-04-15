#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"
"""
super函数的具体用法和场景

父类的MRO列表并遵循如下三条准则：[新式类的继承原则]
子类会先于父类被检查
多个父类会根据它们在列表中的顺序被检查
如果对下一个类存在两个合法的选择，选择第一个父类

super() 函数是子类用于调用父类(超类)的一个方法。

super 是用来解决多重继承问题的，直接用类名调用父类（Base.__init__(self)）方法在使用单继承的时候没问题，
但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题。

MRO 就是类的方法解析顺序表, 其实也就是继承父类方法时的顺序表。



假如说在父类中实现了一个方法，你想在子类中使用父类的这个方法并且做一定扩展但是又不想完全重写，
并且这个场景中的继承属于多继承，那么super()就出场了，可以实现方法的增量修改。


"""


class Base:
    def __init__(self):
        print('Base.__init__')


class A(Base):
    # str_demo = "66"

    def __init__(self):
        super().__init__()
        print('A.__init__')


class B(Base):
    str_demo = "12345"

    def __init__(self):
        super().__init__()
        print('B.__init__')


class C(A, B):
    def __init__(self):
        super().__init__()  # Only one call to super() here
        print('C.__init__')


c = C()
print(c.str_demo)
print(C.__mro__)
