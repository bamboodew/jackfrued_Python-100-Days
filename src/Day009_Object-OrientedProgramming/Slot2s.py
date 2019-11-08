class Person(object):
    __slots__ = ('name', 'gender')  # 规定允许赋值的变量（绑定）


def main():
    person = Person()
    person.name = 'Wang'
    # person.age = 12  # 不允许赋值
    person.gender = 'male'
    print(person.name, person.gender)


if __name__ == '__main__':
    main()
