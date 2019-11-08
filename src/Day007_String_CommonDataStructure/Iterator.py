"""
我们已经知道，可以直接作用于for循环的数据类型有以下几种：
一类是集合数据类型，如list、tuple、dict、set、str等；
一类是generator，包括生成器和带yield的generator function。
这些可以直接作用于for循环的对象统称为【可迭代对象】：Iterable。
可以使用isinstance()判断一个对象是否是Iterable对象：
"""
from collections.abc import Iterable, Iterator


def fib(maxi):
    n, a, b = 0, 0, 1
    while n < maxi:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


def main():
    print(isinstance([], Iterable))
    print(isinstance({}, Iterable))
    print(isinstance((), Iterable))
    print(isinstance('abc', Iterable))
    print(isinstance(fib(10), Iterable))
    print(isinstance((x * x for x in range(10)), Iterable))
    print(isinstance(range(10), Iterable))
    print(isinstance(1000, Iterable))

    """
    而生成器不但可以作用于for循环，还可以被next()
    函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值了。
    可以被next()
    函数调用并不断返回下一个值的对象称为【迭代器】：Iterator。
    可以使用isinstance()
    判断一个对象是否是Iterator对象：
    """
    print()
    print(isinstance([], Iterator))
    print(isinstance({}, Iterator))
    print(isinstance((), Iterator))
    print(isinstance('abc', Iterator))
    print(isinstance(fib(10), Iterator))
    print(isinstance((x * x for x in range(10)), Iterator))
    print(isinstance(range(10), Iterator))
    print(isinstance(1000, Iterator))


if __name__ == '__main__':
    main()
