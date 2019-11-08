'''
Created on 2019年8月28日
输入一个正整数判断它是不是素数
@author: jinshuang1
'''
from math import sqrt

num = int(input('请输入一个整数：'))
end = int(sqrt(num))
is_prime = True

for x in range(2, end + 1):
    if num % x == 0:
        print('%d的因子是%d' % (num, x))
        is_prime = False
        # break
if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)
