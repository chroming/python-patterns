#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
* 一句话总结
通过克隆原型创建新对象实例。
"""


class Prototype(object):

    value = 'default'

    def clone(self, **attrs):
        """克隆原型并更新内部属性字典"""
        obj = self.__class__()
        obj.__dict__.update(attrs)
        return obj


class PrototypeDispatcher(object):

    def __init__(self):
        self._objects = {}

    def get_objects(self):
        """获取所有对象"""
        return self._objects

    def register_object(self, name, obj):
        """注册对象"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """取消注册对象"""
        del self._objects[name]


def main():
    dispatcher = PrototypeDispatcher()
    prototype = Prototype()

    d = prototype.clone()
    a = prototype.clone(value='a-value', category='a')
    b = prototype.clone(value='b-value', is_checked=True)
    dispatcher.register_object('objecta', a)
    dispatcher.register_object('objectb', b)
    dispatcher.register_object('default', d)
    print([{n: p.value} for n, p in dispatcher.get_objects().items()])


if __name__ == '__main__':
    main()

### OUTPUT ###
# [{'objectb': 'b-value'}, {'default': 'default'}, {'objecta': 'a-value'}]
