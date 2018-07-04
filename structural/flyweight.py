#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

* 参考资料
http://codesnipers.com/?q=python-flyweights

* 一句话总结
通过与相似对象共享数据以减少内存占用。

"""

import weakref


class FlyweightMeta(type):

    def __new__(mcs, name, parents, dct):
        """
        设置对象池

        :param name: class name
        :param parents: class parents
        :param dct: dict: includes class attributes, class methods,
        static methods, etc
        :return: new class
        """
        dct['pool'] = weakref.WeakValueDictionary()
        return super(FlyweightMeta, mcs).__new__(mcs, name, parents, dct)

    @staticmethod
    def _serialize_params(cls, *args, **kwargs):
        """
        将参数序列化为一个值。
        最简单的实现是仅仅将其序列化为一个字符串。
        """
        args_list = list(map(str, args))
        args_list.extend([str(kwargs), cls.__name__])
        key = ''.join(args_list)
        return key

    def __call__(cls, *args, **kwargs):
        key = FlyweightMeta._serialize_params(cls, *args, **kwargs)
        pool = getattr(cls, 'pool', {})

        instance = pool.get(key)
        if instance is None:
            instance = super(FlyweightMeta, cls).__call__(*args, **kwargs)
            pool[key] = instance
        return instance


class Card(object):

    """对象池，拥有内建引用计数"""
    _CardPool = weakref.WeakValueDictionary()

    """实现享元模式。如果对象在池中存在则直接返回它（而不是重新创建一个）"""
    def __new__(cls, value, suit):
        obj = Card._CardPool.get(value + suit)
        if not obj:
            obj = object.__new__(cls)
            Card._CardPool[value + suit] = obj
            obj.value, obj.suit = value, suit
        return obj

    # def __init__(self, value, suit):
    #     self.value, self.suit = value, suit

    def __repr__(self):
        return "<Card: %s%s>" % (self.value, self.suit)


def with_metaclass(meta, *bases):
    """Python跨版本元类兼容函数"""
    return meta("NewBase", bases, {})


class Card2(with_metaclass(FlyweightMeta)):

    def __init__(self, *args, **kwargs):
        # print('Init {}: {}'.format(self.__class__, (args, kwargs)))
        pass


if __name__ == '__main__':
    # comment __new__ and uncomment __init__ to see the difference
    c1 = Card('9', 'h')
    c2 = Card('9', 'h')
    print(c1, c2)
    print(c1 == c2, c1 is c2)
    print(id(c1), id(c2))

    c1.temp = None
    c3 = Card('9', 'h')
    print(hasattr(c3, 'temp'))
    c1 = c2 = c3 = None
    c3 = Card('9', 'h')
    print(hasattr(c3, 'temp'))

    # Tests with metaclass
    instances_pool = getattr(Card2, 'pool')
    cm1 =  ('10', 'h', a=1)
    cm2 = Card2('10', 'h', a=1)
    cm3 = Card2('10', 'h', a=2)

    assert (cm1 == cm2) != cm3
    assert (cm1 is cm2) is not cm3
    assert len(instances_pool) == 2

    del cm1
    assert len(instances_pool) == 2

    del cm2
    assert len(instances_pool) == 1

    del cm3
    assert len(instances_pool) == 0

### OUTPUT ###
# (<Card: 9h>, <Card: 9h>)
# (True, True)
# (31903856, 31903856)
# True
# False
