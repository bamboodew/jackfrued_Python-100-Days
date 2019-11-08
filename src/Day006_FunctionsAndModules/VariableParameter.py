'''
Created on 2019年8月30日
# 在参数名前面的*表示args是一个可变参数
# 即在调用add函数时可以传入0个或多个参数
@author: jinshuang1
'''


def add(*args):  # *args默认为一个数列
    total = 0
    for val in range(len(args)):
#         print(val, end=' ')  # 计数index
        total += args[val]
#     print()
    return total


def add_(*args):
    total = 0
    for val in args:  # 可变参数无需range
#         print(val, end=' ')  # 数列的值
        total += val
#     print()
    return total


print(add(1, 3, 5, 7, 9))  # 导入这个模块时，同步执行该行代码

if __name__ == '__main__':  # 导入这个模块时，不执行该段代码
    print(add(1, 3, 5, 7, 9))
    print(add_(1, 3, 5, 7, 9))
