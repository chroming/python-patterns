#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
*用途
在 Java 和其他语言中，抽象工厂模式是为了提供用于创建关联型/依赖型对象的接口，而不需要直接指定他们的具体类。
此模式的主要思想是抽象出可根据不同业务逻辑，平台等创建出不同的对象。
在 Python 中，我们使用的默认接口仅仅是一个可调用对象，并且在通常情况下我们可以简单地将类本身作为此可调用对象，因为类是 Python 中的一等公民。

* 例子含义
此示例实现了根据我们的选择（ Dog 或 Cat ，或 random_animal） ，创建 pet 和其行为的抽象类。
这种方式能正常运行是因为 Dog 和 Cat 均实现了相同的接口（可被创建者调用及 .speak() 方法）。
现在我的程序可以抽象地创建宠物，之后再根据我自己的标准创建 dogs 或 cats 。

* 用处

* 参考资料
https://sourcemaking.com/design_patterns/abstract_factory
http://ginstrom.com/scribbles/2007/10/08/design-patterns-python-style/

* 一句话总结
Provides a way to encapsulate a group of individual factories.
提供了一个封装一组特定工厂类的方式。
"""

import random


class PetShop(object):

    """一个宠物商店"""

    def __init__(self, animal_factory=None):
        """pet_factory 是我们的抽象工厂，我们可以根据按需设定"""

        self.pet_factory = animal_factory

    def show_pet(self):
        """使用抽象工厂创建并显示宠物"""

        pet = self.pet_factory()
        print("We have a lovely {}".format(pet))
        print("It says {}".format(pet.speak()))


class Dog(object):

    def speak(self):
        return "woof"

    def __str__(self):
        return "Dog"


class Cat(object):

    def speak(self):
        return "meow"

    def __str__(self):
        return "Cat"


# 额外的工厂:

# 创建一个随机宠物
def random_animal():
    """动态选择"""
    return random.choice([Dog, Cat])()


# 显示各种宠物
if __name__ == "__main__":

    # 一个只卖猫的宠物店
    cat_shop = PetShop(Cat)
    cat_shop.show_pet()
    print("")

    # 一个卖随机宠物的宠物店
    shop = PetShop(random_animal)
    for i in range(3):
        shop.show_pet()
        print("=" * 20)

### OUTPUT ###
# We have a lovely Cat
# It says meow
# 
# We have a lovely Dog
# It says woof
# ====================
# We have a lovely Cat
# It says meow
# ====================
# We have a lovely Dog
# It says woof
# ====================
