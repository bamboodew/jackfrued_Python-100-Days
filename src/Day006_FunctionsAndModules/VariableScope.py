def foo():
    a = 200  # 局部变量
    global b  # global关键字来指示foo函数中的变量a来自于全局作用域
    b = 200
    print('局部变量a = %d' % a)
    print('局部变量b = %d' % b)


if __name__ == '__main__':
    a = 100
    b = 100
    print('全局变量a = %d' % a)
    print('全局变量b = %d' % b)
    foo()
    print('全局变量a = %d' % a)  # 全局变量不受局部作用
    print('全局变量b = %d' % b)
