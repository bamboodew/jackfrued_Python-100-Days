class Student(object):
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s。' % (self.name, course_name))

    def watch_movie(self):
        if self.age < 18:
            print('%s只能观看《熊出没》。' % self.name)
        else:
            print('%s可以观看岛国爱情动作片。' % self.name)


def main():
    stu1 = Student('Jack', 38)
    stu1.study('Python')
    stu1.watch_movie()

    print()
    stu2 = Student('John', 15)
    stu2.study('Math')
    stu2.watch_movie()


if __name__ == '__main__':
    main()
