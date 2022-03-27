#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "hsz"

"""
python3.7 +

1.coroutine
2.task

调用async main (一个 coroutine function) 的时候返回的是一个 coroutine object
不会运行任何coroutine 里面的代码,会提示： RuntimeWarning: coroutine 'main' was never awaited

运行 coroutine function 的两个条件：
    1.进入async的模式，也就是进入这个event loop开始控制这个程序的状态

    2.把coroutine 变成task

asyncio.run(func_demo())
参数func_demo()就是coroutine
（1）建立起event loop
（2）把coroutine变成event loop的第一个task

synchronize 模块
"""
import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    print(f"started at: {time.strftime('%X')}")
    await say_after(1, 'hello')
    await say_after(2, 'world')
    print(f"finished at {time.strftime('%X')}")


# f0 = main()
asyncio.run(main())
# 首先 main() 放到 event loop 里面，变成 task main
# main 的 await 把 say_after (coroutine function) 得到 coroutine object
# main 需要等待 say_after  
