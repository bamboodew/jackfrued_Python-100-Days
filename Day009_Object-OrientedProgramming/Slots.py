class Person(object):
    # 限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s is playing Flying chess' % self._name)
        else:
            print('%s is playing Fight the landlord' % self._name)


def main():
    person = Person('Wang', 22)
    person.play()
    person._gender = 'male'


if __name__ == '__main__':
    main()
