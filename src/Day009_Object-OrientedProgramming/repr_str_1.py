class A(object):
    def __init__(self, name):
        self._name = name

    @property  # getter
    def name(self):
        return self._name

    def __str__(self):
        return '8'  # 返回'字符串'为实例的值

    # def __repr__(self):
    #     return '9'


def main():
    # a = '123'
    # print(a)
    # print(repr(a))

    b = A('ask')

    print(b)

    print(str(b))
    print(repr(b))  # <__main__.A object at 0x02D7FA10>

    print('%s' % b)
    print('%r' % b)  # <__main__.A object at 0x02D7FA10>

    print(b.__str__())
    print(b.__repr__())  # <__main__.A object at 0x02D7FA10>
    # print(b.name)S


if __name__ == '__main__':
    main()
