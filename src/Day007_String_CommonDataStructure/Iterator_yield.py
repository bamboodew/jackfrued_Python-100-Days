def main():
    print('starting...')
    while True:
        res = yield 4
        print('res:', res)


if __name__ == '__main__':
    # foo中有yield，所以foo不会真正执行，而是得到一个生成器g(相当于一个对象)
    g = main()
    # 调用next方法，foo函数正式开始执行，先执行foo函数中的print方法，然后进入while循环
    # 程序遇到yield关键字，然后把yield想想成return, return了一个4之后，程序停止，并没有执行赋值给res操作，此时next(g)
    # 语句执行完成，所以输出的前两行。
    print(next(g))
    # 程序执行print("*" * 20)，输出20个 *
    print("*" * 20)
    # 又开始执行下面的print(next(g)), 这个时候和上面那个差不多，不过不同的是，这个时候是从刚才那个next程序停止的地方开始执行的，也就是要执行res
    # 的赋值操作，这时候要注意，这个时候赋值操作的右边是没有值的（因为刚才那个是return出去了，并没有给赋值操作的左边传参数），
    # 所以这个时候res赋值是None, 所以接着下面的输出就是res: None
    # 程序会继续在while里执行，又一次碰到yield, 这个时候同样return出4，然后程序停止，print函数输出的4就是这次return出的4.
    print(next(g))
