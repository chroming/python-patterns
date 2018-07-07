#!/usr/bin/env python
# -*- coding: utf-8 -*-


class RegistryHolder(type):

    REGISTRY = {}

    def __new__(cls, name, bases, attrs):
        new_cls = type.__new__(cls, name, bases, attrs)
        """
            此处使用类名作为键，你也可以用其他任何类的参数。
        """
        cls.REGISTRY[new_cls.__name__] = new_cls
        return new_cls

    @classmethod
    def get_registry(cls):
        return dict(cls.REGISTRY)


class BaseRegisteredClass(object):
    __metaclass__ = RegistryHolder
    """
        所有继承 BaseRegisteredClass 的类都包含内置的字典 RegistryHolder.REGISTRY，
        键是类名，值是类本身。
    """
    pass

if __name__ == "__main__":
    print("Before subclassing: ")
    for k in RegistryHolder.REGISTRY:
        print(k)

    class ClassRegistree(BaseRegisteredClass):

        def __init__(self, *args, **kwargs):
            pass

    print("After subclassing: ")
    for k in RegistryHolder.REGISTRY:
        print(k)

###  OUTPUT ###
# Before subclassing:
# BaseRegisteredClass
# After subclassing:
# BaseRegisteredClass
# ClassRegistree
