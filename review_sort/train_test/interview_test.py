#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"
"""
1..python新式类和经典类的区别？
    a. 在python里凡是继承了object的类，都是新式类
    b. Python3里只有新式类
    c. Python2里面继承object的是新式类，没有写父类的是经典类
    d. 经典类目前在Python里基本没有应用
    e. 保持class与type的统一对新式类的实例执行a.class与type(a)的结果是一致的，对于旧式类来说就不
    一样了。
    f.对于多重继承的属性搜索顺序不一样:
        新式类是采用广度优先搜索，
        旧式类采用深度优先搜索。

2..python中内置的数据结构有几种？
    a. 整型 int、 长整型 long、浮点型 float、 复数 complex
    b. 字符串 str、 列表 list、 元祖 tuple
    c. 字典 dict 、 集合 set
    d. Python3 中没有 long，只有无限精度的 int

3.python如何实现单例模式?请写出两种实现方式?
https://www.cnblogs.com/panlq/p/12355917.html
第一种方法:使用装饰器
def singleton(cls):
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
            return instances[cls]

    return wrapper


@singleton
class Foo(object):
    pass


foo1 = Foo()
foo2 = Foo()
print(id(foo1) == id(foo1))  # 这个不知道为什么不相等



# 第二种方法：使用基类
class Singleton(object):
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls.instance


t1 = Singleton()
t2 = Singleton()
print(id(t1) == id(t2))

'''
第三种方法：元类，元类是用于创建类对象的类，类对象创建实例对象时一定要调用call方法，因此在
调用call时候保证始终只创建一个实例即可，type是python的元类
'''
class Singleton(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]


# python2写法
# class MyClass(object):
#     __metaclass__ = Singleton()

# python3写法
class MyClass(metaclass=Singleton):
    def __init__(self):
        self.blog = "blog"


t1 = MyClass()
t2 = MyClass()
print(id(t1) == id(t2))

4.可变类型和不可变类型
1,可变类型有list,dict,set.不可变类型有string，number,tuple.
2,当进行修改操作时，可变类型传递的是内存中的地址，也就是说，直接修改内存中的值，并没有开辟
新的内存。
3,不可变类型被改变时，并没有改变原内存地址中的值，而是开辟一块新的内存，将原地址中的值复制
过去，对这块新开辟的内存中的值进行操作。

5.is和==有什么区别？
is：比较的是两个对象的id值是否相等，也就是比较俩对象是否为同一个实例对象。是否指向同一个内
存地址
== ： 比较的两个对象的内容/值是否相等，默认会调用对象的eq()方法

6.Python中变量的作用域？（变量查找顺序)
函数作用域的LEGB顺序
1.什么是LEGB?
L： local 函数内部作用域（内函数的变量）
E: enclosing 函数内部与内嵌函数之间(外函数的变量)
G: global 全局作用域（全局变量）
B： build-in 内置作用（文件内置的变量）
python在函数里面的查找分为4种，称之为LEGB，也正是按照这是顺序来查找的

7.阅读一下代码他们的输出结果是什么？
def multi():
    return [lambda x: i * x for i in range(4)]


print([m(3) for m in multi()])

正确答案是[9,9,9,9]，而不是[0,3,6,9]产生的原因是Python的闭包的后期绑定导致的，这意味着在闭包
中的变量是在内部函数被调用的时候被查找的，因为，最后函数被调用的时候，for循环已经完成, i 的
值最后是3,因此每一个返回值的i都是3,所以最后的结果是[9,9,9,9]

8..简述read、readline、readlines的区别？
read 读取整个文件
readline 读取下一行
readlines 读取整个文件到一个迭代器以供我们遍历

9.编写函数的4个原则
1.函数设计要尽量短小
2.函数声明要做到合理、简单、易于使用
3.函数参数设计应该考虑向下兼容
4.一个函数只做一件事情，尽量保证函数语句粒度的一致性

10.函数调用参数的传递方式是值传递还是引用传递？

Python的参数传递有：位置参数、默认参数、可变参数、关键字参数。
函数的传值到底是值传递还是引用传递、要分情况：
不可变参数用值传递：像整数和字符串这样的不可变对象，是通过拷贝进行传递的，因为你无论如何都
不可能在原处改变不可变对象。
可变参数是引用传递：比如像列表，字典这样的对象是通过引用传递、和C语言里面的用指针传递数组
很相似，可变对象能在函数内部改变。



8.简述Python里面search和match的区别
match()函数只检测字符串开头位置是否匹配，匹配成功才会返回结果，否则返回None； 
search()函数会在整个字符串内查找模式匹配,只到找到第一个匹配然后返回一个包含匹配信息的对象,
该对象可以通过调用group()方法得到匹配的字符串,如果字符串没有匹配，则返回None。


9.Python中类方法、类实例方法、静态方法有何区别？
类方法: 是类对象的方法，在定义时需要在上方使用 @classmethod 进行装饰,形参为cls，表示类对象，
类对象和实例对象都可调用
类实例方法: 是类实例化对象的方法,只有实例对象可以调用，形参为self,指代对象本身;
静态方法: 是一个任意函数，在其上方使用 @staticmethod 进行装饰，可以用对象直接调用，静态方法
实际上跟该类没有太大关系

10.如何在function里面设置一个全局变量
globals() # 返回包含当前作用余全局变量的字典。 global 变量 设置使用全局变量

11.对缺省参数的理解 ？
缺省参数指在调用函数的时候没有传入参数的情况下，调用默认的参数，在调用函数的同时赋值时，所
传入的参数会替代默认参数。
*args是不定长参数，它可以表示输入参数是不确定的，可以是任意多个。
**kwargs是关键字参数，赋值的时候是以键值对的方式，参数可以是任意多对在定义函数的时候
不确定会有多少参数会传入时，就可以使用两个参数


哪些操作会导致Python内存溢出，怎么处理？
循环引用，手动释放


10.Python的内存管理机制及调优手段？
内存管理机制: 引用计数、垃圾回收、内存池
引用计数：引用计数是一种非常高效的内存管理手段，当一个Python对象被引用时其引用计数增加1,
当其不再被一个变量引用时则计数减1,当引用计数等于0时对象被删除。弱引用不会增加引用计数
垃圾回收：
1.引用计数
引用计数也是一种垃圾收集机制，而且也是一种最直观、最简单的垃圾收集技术。当Python的某个对象
的引用计数降为0时，说明没有任何引用指向该对象，该对象就成为要被回收的垃圾了。比如某个新建
对象，它被分配给某个引用，对象的引用计数变为1，如果引用被删除，对象的引用计数为0,那么该对
象就可以被垃圾回收。不过如果出现循环引用的话，引用计数机制就不再起有效的作用了。
2.标记清除
https://foofish.net/python-gc.html
调优手段
1.手动垃圾回收
2.调高垃圾回收阈值
3.避免循环引用


11.内存泄露是什么？如何避免？
    内存泄漏指由于疏忽或错误造成程序未能释放已经不再使用的内存。内存泄漏并非指内存在物理上的消
失，而是应用程序分配某段内存后，由于设计错误，导致在释放该段内存之前就失去了对该段内存的控
制，从而造成了内存的浪费。

    有 __del__() 函数的对象间的循环引用是导致内存泄露的主凶。不使用一个对象时使用: del object 来
删除一个对象的引用计数就可以有效防止内存泄露问题。
通过Python扩展模块gc 来查看不能回收的对象的详细信息。
可以通过 sys.getrefcount(obj) 来获取对象的引用计数，并根据返回值是否为0来判断是否内存泄露


12.谈谈你对多进程，多线程，以及协程的理解，项目是否用？
这个问题被问的概念相当之大，
    进程：一个运行的程序（代码）就是一个进程，没有运行的代码叫程序，进程是系统资源分配的最小单
位，进程拥有自己独立的内存空间，所有进程间数据不共享，开销大。
    线程: cpu调度执行的最小单位，也叫执行路径，不能独立存在，依赖进程存在，一个进程至少有一个线
程，叫主线程，而多个线程共享内存（数据共享，共享全局变量),从而极大地提高了程序的运行效率。
    协程: 是一种用户态的轻量级线程，协程的调度完全由用户控制。协程拥有自己的寄存器上下文和栈。
协程调度时，将寄存器上下文和栈保存到其他地方，在切回来的时候，恢复先前保存的寄存器上下文和
栈，直接操中栈则基本没有内核切换的开销，可以不加锁的访问全局变量，所以上下文的切换非常快。

SS


1. dict实现 扩容机制 
2. weakref 
3. celery内存泄漏 
4. MySQL索引失效 
5. 间隙锁 如何解决幻读 
6. 慢查询 
7.python内存管理 
8. 野指针 
9. MySQL bigint大小 
10. MySQL5.7 8.0区别 
11.redis持久化 
12. cow 持久化流程 
13. 内核优化 
14.大数据量优化 
15.归并算法 布隆过滤器 flask底层流程 nginx-gunicorn-python关系
16.requests线程安全问题
另一家的ng穿透 多个ng漂移如何获取真实ip 100g文件2g内存处理文件 http各版本区别 bitmap算法 跳台阶算法  lru实现


希尔排序？桶排序？前中后序数，链反转？lru, kmp？
"""
# if hasattr(Parent, 'x'):
#     print(getattr(Parent, 'x'))
#     setattr(Parent, 'x',3)
#     print(getattr(Parent,'x'))


from math import ceil

print(ceil(0.5))
