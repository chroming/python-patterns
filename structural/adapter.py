#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
* 解释
适配器模式将类转换为另一种接口。我们可以将其看作允许你使用不兼容插口给你手机充电的电源转换器。
以这种概念来考虑，适配器模式可以整合因接口不兼容原本无法整合的类。

* 例子含义
示例中包含不同的实物类（Dog，Cat，Human，Car），会发出不同的声音。
接口类将这些原本不同的声音方法转换为另一种通用方法，
因此这些不同的方法最后都可以用 make_noise 这一方法名调用。

* 用处
Grok 框架使用接口模式以在不修改对象的前提下提供另一种API：
http://grok.zope.org/doc/current/grok_overview.html#adapters

* 参考资料
http://ginstrom.com/scribbles/2008/11/06/generic-adapter-class-in-python/
https://sourcemaking.com/design_patterns/adapter
http://python-3-patterns-idioms-test.readthedocs.io/en/latest/ChangeInterface.html#adapter

* 一句话总结
允许一个已有类的接口以另一种方式调用。
"""


class Dog(object):

    def __init__(self):
        self.name = "Dog"

    def bark(self):
        return "woof!"


class Cat(object):

    def __init__(self):
        self.name = "Cat"

    def meow(self):
        return "meow!"


class Human(object):

    def __init__(self):
        self.name = "Human"

    def speak(self):
        return "'hello'"


class Car(object):

    def __init__(self):
        self.name = "Car"

    def make_noise(self, octane_level):
        return "vroom{0}".format("!" * octane_level)


class Adapter(object):
    """
    通过替换方法适配一个对象。
    使用方式:
    dog = Dog()
    dog = Adapter(dog, make_noise=dog.bark)

    >>> objects = []
    >>> dog = Dog()
    >>> print(dog.__dict__)
    {'name': 'Dog'}
    >>> objects.append(Adapter(dog, make_noise=dog.bark))
    >>> print(objects[0].original_dict())
    {'name': 'Dog'}
    >>> cat = Cat()
    >>> objects.append(Adapter(cat, make_noise=cat.meow))
    >>> human = Human()
    >>> objects.append(Adapter(human, make_noise=human.speak))
    >>> car = Car()
    >>> car_noise = lambda: car.make_noise(3)
    >>> objects.append(Adapter(car, make_noise=car_noise))

    >>> for obj in objects:
    ...     print('A {} goes {}'.format(obj.name, obj.make_noise()))
    A Dog goes woof!
    A Cat goes meow!
    A Human goes 'hello'
    A Car goes vroom!!!
    """

    def __init__(self, obj, **adapted_methods):
        """We set the adapted methods in the object's dict"""
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        """All non-adapted calls are passed to the object"""
        return getattr(self.obj, attr)

    def original_dict(self):
        """Print original object dict"""
        return self.obj.__dict__

def main():

    objects = []
    dog = Dog()
    print(dog.__dict__)
    objects.append(Adapter(dog, make_noise=dog.bark))
    print(objects[0].__dict__)
    print(objects[0].original_dict())
    cat = Cat()
    objects.append(Adapter(cat, make_noise=cat.meow))
    human = Human()
    objects.append(Adapter(human, make_noise=human.speak))
    car = Car()
    objects.append(Adapter(car, make_noise=lambda: car.make_noise(3)))

    for obj in objects:
        print("A {0} goes {1}".format(obj.name, obj.make_noise()))


if __name__ == "__main__":
    main()

### OUTPUT ###
# {'name': 'Dog'}
# {'make_noise': <bound method Dog.bark of <__main__.Dog object at 0x7f631ba3fb00>>, 'obj': <__main__.Dog object at 0x7f631ba3fb00>}
# {'name': 'Dog'}
# A Dog goes woof!
# A Cat goes meow!
# A Human goes 'hello'
# A Car goes vroom!!!
