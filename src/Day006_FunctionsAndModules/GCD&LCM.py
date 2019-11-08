"""
Created on 2019年8月30日

@author: jinshuang1
"""
from math import sqrt


def gcd(x, y):
    print('starting...')
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            print('yield')
            yield factor  # 返回之后就停止for循环


def lcm(x, y):
    return x * y // gcd(x, y)


def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    if total == num:
        return '是回文数'
    else:
        return '不是回文数'
    # return total == num


def is_prime(num):
    for factor in range(2, int(sqrt(num) + 1)):
        if num % factor == 0:
            return False
    return True if num != 1 else False


if __name__ == '__main__':  # 导入时不执行该段代码块
    f = gcd(108, 120)
    print(f)
    # print(gcd(108, 120))
    # print(next(gcd(108, 120)))
    # print(next(gcd(108, 120)))
    x, y = 108, 120
    (x, y) = (y, x) if x > y else (x, y)
    # for factor in range(x, 0, -1):
    #     if x % factor == 0 and y % factor == 0:
    #         print(factor)  # 返回之后，继续执行循环直至结束

    s = int(input('请输入：'))
    print('%d%s' % (s, is_palindrome(s)))  # 判断是否为回文数

    a = int(input('请输入：'))
    print(is_prime(a))  # 判断是否为素数

    b = int(input('请输入：'))
    if is_palindrome(b) and is_prime(b):
        print('%d是回文素数' % b)
    else:
        print('%d不是回文素数' % b)


