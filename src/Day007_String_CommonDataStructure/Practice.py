import random


def get_suffix(fileName):
    return fileName[(fileName.find('.') + 1):]


def get_emailWeb(emailName):
    return emailName[(emailName.find('@') + 1):(emailName.find('.'))]


def max2(li):
    m1, m2 = (li[0], li[1]) if li[0] > li[1] else (li[1], li[0])
    for index in range(2, len(li)):  # ser
        if li[index] > m1:
            m2 = m1
            m1 = li[index]
        elif li[index] > m2:
            m2 = li[index]
    return m1, m2  # 以元组形式输出


def is_leapYear(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def which_day(year, month, date):
    days_of_month = [[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
                     [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                     ][is_leapYear(year)]  # 此处的is_leapYear(year)是索引：0或1
    total = 0
    for index in range(month - 1):
        total += days_of_month[index]
    return total + date


def changeEle(t, i, e):  # 将元组的第i个元素值改为e，返回一个新元组
    list1 = list(t)
    list1[i] = e
    t = tuple(list1)
    return t


def main():
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code = ''
    for _ in range(10):
        index = random.randint(0, len(all_chars) - 1)
        code += all_chars[index]
    print('随机验证码:', code)
    print(get_suffix('mrbamboodew@163.com'), '文件')
    print(get_emailWeb('mrbamboodew@qq.com'), '邮箱')
    print(max2([1, 3, 9, 4, 6, 20]))
    print(which_day(2020, 12, 31))

    tuple1 = (12, 13, 14, 15)
    tuple2 = changeEle(changeEle(tuple1, 1, 16), 0, 100)
    print('tuple2 =', tuple2)
    print('tuple1 =', tuple1)  # 函数不能改全局变量的值
    print(*tuple1)
    list1 = [12, 13, 14, 15]
    print(*list1)
    for i in list1:
        print(i, end=' ')

    # 打印杨辉三角
    num = int(input('请输入行数：'))
    yh = [[]] * num  # num行数列
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()


if __name__ == '__main__':
    main()
