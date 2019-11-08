class A(object):
    def __init__(self, name):
        self._name = name

    @property  # getter
    def name(self):
        return self._name

    # def __str__(self):
    #     return '8'  # 返回'字符串'为实例的值

    def __repr__(self):
        return '9'


def main():
    # a = '123'
    # print(a)
    # print(repr(a))

    b = A('ask')

    print(b)

    print(str(b))  # output: 9
    print(repr(b))

    print('%s' % b)  # output: 9
    print('%r' % b)

    print(b.__str__())  # output: 9
    print(b.__repr__())

    # print(b.name)


if __name__ == '__main__':
    main()
