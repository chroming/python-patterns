#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
* 解释
此模式用于创建一类对象的消耗较高时（且经常需要新建此对象）但同一时间只需使用一小部分对象的情况。
使用一个对象池我们可以通过缓存机制管理当前已有的实例。当对象池中已有某个对象时我们就可以减少新建成本。
一个对象池经常需要“检出”一个非活跃对象并返回它。当对象池为空时则直接新建对象。

* 例子含义
示例中 queue.Queue 用于创建对象池（使用一个自定义的 ObjectPool 对象使其支持 with 语法），并使用字符串填充它。
我们可以看到，第一个字符串 “yam” 被 with 语法使用了，但因为它在被释放后会回到对象池中，
它在随后的 sample_queue.get() 又重新出现了。“sam” 字符串同理。

* 用处

* 参考资料
http://stackoverflow.com/questions/1514120/python-implementation-of-the-object-pool-design-pattern
https://sourcemaking.com/design_patterns/object_pool

* 一句话总结
保存一系列已初始化的对象以便随时使用。
"""


class ObjectPool(object):

    def __init__(self, queue, auto_get=False):
        self._queue = queue
        self.item = self._queue.get() if auto_get else None

    def __enter__(self):
        if self.item is None:
            self.item = self._queue.get()
        return self.item

    def __exit__(self, Type, value, traceback):
        if self.item is not None:
            self._queue.put(self.item)
            self.item = None

    def __del__(self):
        if self.item is not None:
            self._queue.put(self.item)
            self.item = None


def main():
    try:
        import queue
    except ImportError:  # python 2.x 兼容写法
        import Queue as queue

    def test_object(queue):
        pool = ObjectPool(queue, True)
        print('Inside func: {}'.format(pool.item))

    sample_queue = queue.Queue()

    sample_queue.put('yam')
    with ObjectPool(sample_queue) as obj:
        print('Inside with: {}'.format(obj))
    print('Outside with: {}'.format(sample_queue.get()))

    sample_queue.put('sam')
    test_object(sample_queue)
    print('Outside func: {}'.format(sample_queue.get()))

    if not sample_queue.empty():
        print(sample_queue.get())


if __name__ == '__main__':
    main()

### OUTPUT ###
# Inside with: yam
# Outside with: yam
# Inside func: sam
# Outside func: sam
