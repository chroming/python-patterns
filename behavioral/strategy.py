#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
http://stackoverflow.com/questions/963965/how-is-this-strategy-pattern
 -written-in-python-the-sample-in-wikipedia
在许多其他语言中策略模式是通过创建策略基类/接口并子类化大量具体策略类来实现的（
可见http://en.wikipedia.org/wiki/Strategy_pattern），然而 Python 支持高级函数，
允许我们仅使用单个类并传入不同函数，正如示例那样。

*一句话总结
允许在运行时选择算法。
"""

import types


class StrategyExample:

    def __init__(self, func=None):
        self.name = 'Strategy Example 0'
        if func is not None:
            self.execute = types.MethodType(func, self)

    def execute(self):
        print(self.name)


def execute_replacement1(self):
    print(self.name + ' from execute 1')


def execute_replacement2(self):
    print(self.name + ' from execute 2')


if __name__ == '__main__':
    strat0 = StrategyExample()

    strat1 = StrategyExample(execute_replacement1)
    strat1.name = 'Strategy Example 1'

    strat2 = StrategyExample(execute_replacement2)
    strat2.name = 'Strategy Example 2'

    strat0.execute()
    strat1.execute()
    strat2.execute()

### OUTPUT ###
# Strategy Example 0
# Strategy Example 1 from execute 1
# Strategy Example 2 from execute 2
