from functools import reduce


def f(x):
    return x ** 2


def add(x, y):
    return x + y


def main():
    print(f(10))
    list1 = [1, 2, 3, 4, 5]
    iterator1 = map(f, list1)
    print(iterator1)
    # print(list(iterator1))

    # print(tuple(iterator1))  # iterator只能经过一次遍历

    # for i in iterator1:
    #     print(i, end=' ')

    print(set(iterator1))
    print(list(map(str, list1)))  # 把列表的所有元素转换为字符串

    """
    再看reduce的用法。
    reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
    这个函数必须接收两个参数，
    reduce把结果继续和序列的下一个元素做累积计算
    """
    print(reduce(add, [1, 2, 3, 4, 5]))


if __name__ == '__main__':
    main()
