class A(object):
    def __init__(self, name):
        self._name = name

    @property  # getter
    def name(self):
        return self._name

    # def __repr__(self):
    #     return 'A_repr'

    def __str__(self):
        return 'A_str'  # 返回'字符串'为实例的值


class B(A):
    def __init__(self, name):
        super().__init__(name)

    # def __repr__(self):
    #     return 'B_repr'

    def __str__(self):
        return 'B_str'


def main():
    a = A('ask')
    b = B('blue')
    # print('a:', a)
    print('repr(a):', repr(a))
    print('str(a):', str(a))
    print()
    # print('b:', b)
    print('repr(b):', repr(b))
    print('str(b):', str(b))


if __name__ == '__main__':
    main()