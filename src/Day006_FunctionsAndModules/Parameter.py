'''
Created on 2019年8月30日
函数是绝大多数编程语言中都支持的一个代码的“构建块”，
但是Python中的函数与其他语言中的函数还是有很多不太相同的地方，
其中一个显著的区别就是Python对函数参数的处理。
在Python中，函数的参数可以有默认值，也支持使用可变参数，
所以Python并不需要像其他语言一样支持函数的重载，
因为我们在定义一个函数的时候可以让它有多种不同的使用方式，下面是两个小例子。
@author: jinshuang1
'''
from random import randint

'''
摇骰子
:param n: 色子的个数
:return: n颗色子点数之和
'''


def roll_dice(n=2):
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total


def add(a=0, b=0, c=0):
    return a + b * 2 + c * 3


print(roll_dice())
print(roll_dice(4))

print(add())
print(add(1, 2, 3))
print(add(c=1, b=2, a=3))  # 参数位置可以手动调整
