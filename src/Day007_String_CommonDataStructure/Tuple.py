def change(i, s):
    l = list(t)
    l[i] = s
    return tuple(l)


def main():
    # tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
    # t = ('骆昊', 38, True, '四川成都')
    print('元组: ', t)
    print(t[::-1])
    for member in t:
        print(member, end=' ')

    print()
    tuple1 = ('王大锤', 20, True, '云南昆明')
    print(tuple1)
    list1 = list(tuple1)
    print(list1)
    # tuple1[0] = '张三'  # TypeError: 'tuple' object does not support item assignment
    list1[0] = '张三'
    print(list1)
    print(tuple(list1))

    tuple2 = () * 10
    print(tuple2)
    t2 = change(-1, '广东佛山')
    print(t2)


if __name__ == '__main__':
    t = ('骆昊', 38, True, '四川成都')
    main()
