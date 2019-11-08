class Person(object):
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
        print('%s is playing happily.' % self._name)

    def watch_av(self):
        if self._age >= 18:
            print('%s is watching av.' % self._name)
        else:
            print('%s is watching cartoon.' % self._name)


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print('%s的%s正在学习%s.' % (self._grade, self._name, course))


class Teacher(Person):
    def __init__(self, name, age, title):
        super().__init__(name, age)  # 继承、借用属性/方法
        self._title = title  # 增加特有属性

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print('%s %s正在讲%s.' % (self._name, self._title, course))


def main():
    stu = Student('Wang', 15, '初三')
    stu.study('Math')
    stu.watch_av()
    teacher = Teacher('Luo', 38, '专家')
    teacher.teach('Python')
    teacher.watch_av()


if __name__ == '__main__':
    main()
