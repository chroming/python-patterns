#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
*用途
Borg 模式（亦被称为 Monostate 模式）是一种实现单例模式效果，但拥有多个实例并在他们之间共享状态的设计模式。
换句话说，此模式的目的是共享实例间状态而不是共享单个实例。

* 例子含义
要理解此模式在 Python 中的实现，首先要明白在 Python 中实例属性均存储在__dict__字典中。
通常情况下，实例字典只保存其自身的属性，但 Borg 模式修改了这部分，使得实例间共享同个字典。
在示例中，__shared_state 属性是在实例中共享的，这是通过在实例化时将 __shared_state 赋值给
__dict__ 实现的（比如在 __init__ 方法中赋值）。其他属性如往常一样添加到实例的属性字典中，
但由于属性字典本身是共享的（即 __shared_state），所有其他属性也会被共享。
因此，当 rm2 中的 self.state 属性被修改时，rm1 中的此属性也会被修改。子类的实例 rm3 也是同理。
注意，即使这些实例共享属性，他们也是不同的对象，可通过检查id来证明。

* 用处
共享状态在一些应用，比如管理数据库连接中常用：
https://github.com/onetwopunch/pythonDbTemplate/blob/master/database.py

* 参考资料
https://fkromer.github.io/python-pattern-references/design/#singleton

* 一句话总结
通过在实例间共享状态以提供类似单例模式的性质。

"""


class Borg(object):
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.state = 'Init'

    def __str__(self):
        return self.state


class YourBorg(Borg):
    pass


if __name__ == '__main__':
    rm1 = Borg()
    rm2 = Borg()

    rm1.state = 'Idle'
    rm2.state = 'Running'

    print('rm1: {0}'.format(rm1))
    print('rm2: {0}'.format(rm2))

    rm2.state = 'Zombie'

    print('rm1: {0}'.format(rm1))
    print('rm2: {0}'.format(rm2))

    print('rm1 id: {0}'.format(id(rm1)))
    print('rm2 id: {0}'.format(id(rm2)))

    rm3 = YourBorg()

    print('rm1: {0}'.format(rm1))
    print('rm2: {0}'.format(rm2))
    print('rm3: {0}'.format(rm3))

### OUTPUT ###
# rm1: Running
# rm2: Running
# rm1: Zombie
# rm2: Zombie
# rm1 id: 140732837899224
# rm2 id: 140732837899296
# rm1: Init
# rm2: Init
# rm3: Init
