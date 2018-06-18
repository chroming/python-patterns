#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
* 解释
工厂方法模式可为方法创建接口，并将具体实例化过程交由类来实现。

* 例子含义
示例代码展示了一种将本地语言翻译为英文和希腊文的方式。
"getLocalizer" 是根据选择的语言构造相应翻译器实例的工厂方法。
翻译器对象是与所选语言对应的类实例。
然而，主函数不需要考虑应实例化哪个语言类，因为所有类都实现了 get 方法。


* 用处
流行的框架 Django 中用到了工厂方法模式：http://django.wikispaces.asu.edu/*NEW*+Django+Design+Patterns 。
比如，在一个页面的联系人表单中，标题和信息字典使用了相同的表单工厂（CharField()），即使他们因目的不同有着不同的实现方式。

* 参考资料
http://ginstrom.com/scribbles/2007/10/08/design-patterns-python-style/
https://fkromer.github.io/python-pattern-references/design/#factory-method
https://sourcemaking.com/design_patterns/factory_method

* 一句话总结
无需明确指定类即可创建特定对象。

"""


class GreekGetter(object):

    """简单的希腊语翻译器类"""

    def __init__(self):
        self.trans = dict(dog="σκύλος", cat="γάτα")

    def get(self, msgid):
        """We'll punt if we don't have a translation"""
        return self.trans.get(msgid, str(msgid))


class EnglishGetter(object):

    """单纯返回消息id"""

    def get(self, msgid):
        return str(msgid)


def get_localizer(language="English"):
    """工厂方法"""
    languages = dict(English=EnglishGetter, Greek=GreekGetter)
    return languages[language]()


if __name__ == '__main__':
    # 创建翻译器实例
    e, g = get_localizer(language="English"), get_localizer(language="Greek")
    # 翻译文字
    for msgid in "dog parrot cat bear".split():
        print(e.get(msgid), g.get(msgid))

### OUTPUT ###
# dog σκύλος
# parrot parrot
# cat γάτα
# bear bear
