class A(object):
    def __init__(self, name):
        self._name = name

    @property  # getter
    def name(self):
        return self._name

    def __str__(self):
        return 'A_str'  # 返回'字符串'为实例的值

    # def __repr__(self):
    #     return 'A_repr'


class B(A):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return 'B_str'

    # def __repr__(self):
    #     return 'B_repr'


def main():
    # a = '123'
    # print(a)
    # print(repr(a))

    a = A('ask')
    b = B('blue')
    print(a)
    print(str(a))
    print(repr(a))
    print('%s' % a)
    print('%r' % a)
    print(a.__str__())
    print(a.__repr__())
    print()

    print(b)
    print(str(b))
    print(repr(b))


if __name__ == '__main__':
    main()
