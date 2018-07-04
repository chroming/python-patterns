#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
* 解释
外观模式为复杂系统提供简单的统一接口。它通过单个接入点提供访问基础系统的简易方式。
这种抽象在生活中很常见。比如我们只需按一下电脑的开关就可以启动电脑，但实际上，背后有许多程序和
操作会在启动时完成（比如，将程序从磁盘中载入内存）。也就是说，这个按钮就是一个启动电脑的统一接口。

* 例子含义
示例定义了三个类（TC1, TC2, TC3)代表要被测试的复杂组件。
TestRunner 类以外观模式运行，通过一个 runAll 方法运行所有测试。
之后，客户端只需实例化 TestRunner 并调用 runAll 方法即可。
正如示例中所示，外观模式提供的接口独立于基础实现。
由于客户端只是单纯调用 runAll 方法，我们可以在不影响客户端调用的情况下
修改 TC1, TC2, TC3 类。

* 用处
此模式可以在使用Python标准库中的isdir函数时发现。
尽管用户使用此函数只是简单地想知道一个路径是否是目录，
但系统在背后仍然做了一些操作，并通过调用一些其他模块来
获取结果。


* 参考资料
https://sourcemaking.com/design_patterns/facade
https://fkromer.github.io/python-pattern-references/design/#facade
http://python-3-patterns-idioms-test.readthedocs.io/en/latest/ChangeInterface.html#facade


* 一句话总结
为复杂系统提供一个简单的统一接口。

"""

from __future__ import print_function
import time

SLEEP = 0.1


# 复杂组件
class TC1:

    def run(self):
        print(u"###### In Test 1 ######")
        time.sleep(SLEEP)
        print(u"Setting up")
        time.sleep(SLEEP)
        print(u"Running test")
        time.sleep(SLEEP)
        print(u"Tearing down")
        time.sleep(SLEEP)
        print(u"Test Finished\n")


class TC2:

    def run(self):
        print(u"###### In Test 2 ######")
        time.sleep(SLEEP)
        print(u"Setting up")
        time.sleep(SLEEP)
        print(u"Running test")
        time.sleep(SLEEP)
        print(u"Tearing down")
        time.sleep(SLEEP)
        print(u"Test Finished\n")


class TC3:

    def run(self):
        print(u"###### In Test 3 ######")
        time.sleep(SLEEP)
        print(u"Setting up")
        time.sleep(SLEEP)
        print(u"Running test")
        time.sleep(SLEEP)
        print(u"Tearing down")
        time.sleep(SLEEP)
        print(u"Test Finished\n")


# 外观模式
class TestRunner:

    def __init__(self):
        self.tc1 = TC1()
        self.tc2 = TC2()
        self.tc3 = TC3()
        self.tests = [self.tc1, self.tc2, self.tc3]

    def runAll(self):
        [i.run() for i in self.tests]


# 客户端
if __name__ == '__main__':
    testrunner = TestRunner()
    testrunner.runAll()

### OUTPUT ###
# ###### In Test 1 ######
# Setting up
# Running test
# Tearing down
# Test Finished
#
# ###### In Test 2 ######
# Setting up
# Running test
# Tearing down
# Test Finished
#
# ###### In Test 3 ######
# Setting up
# Running test
# Tearing down
# Test Finished
#
