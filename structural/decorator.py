#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
* 解释
装饰器模式用于在不修改对象实现的情况下给它动态添加一个新特性。
这与继承不同，因为它仅仅修改特定对象，而不是全部子类。

* 例子含义
示例展示了一种通过附加相应标签（<b>和<i>）来添加格式化选项的方式。
同时，我们能注意到不同的装饰器可以一个接着一个地作用于同个对象，
在原始文本被传递给加粗装饰器后接着又被传递给斜体装饰器。

* 用处
Grok 框架使用装饰器给方法添加功能，比如给事件添加权限或订阅功能：
http://grok.zope.org/doc/current/reference/decorators.html

* 参考资料
https://sourcemaking.com/design_patterns/decorator

* 一句话总结
在不修改对象实现的情况下给对象添加功能。

"""

from __future__ import print_function

class TextTag(object):
    """基础文本标签"""
    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text


class BoldWrapper(TextTag):
    """使用<b>装饰标签"""
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return "<b>{}</b>".format(self._wrapped.render())


class ItalicWrapper(TextTag):
    """使用<i>装饰标签"""
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return "<i>{}</i>".format(self._wrapped.render())

if __name__ == '__main__':
    simple_hello = TextTag("hello, world!")
    special_hello = ItalicWrapper(BoldWrapper(simple_hello))
    print("before:", simple_hello.render())
    print("after:", special_hello.render())

### OUTPUT ###
# before: hello, world!
# after: <i><b>hello, world!</b></i>
