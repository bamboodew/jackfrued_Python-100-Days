'''
Created on 2019年8月28日
输入两个正整数计算最大公约数和最小公倍数

@author: jinshuang1
'''

x = int(input('x='))
y = int(input('y='))

if x > y:
    x, y = y, x
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公约数是%d' % (x, y, factor))
        print('%d和%d的最小公倍数是%d' % (x, y, x * y / factor))  # 最小公倍数=最小公约数*X*Y
        break
