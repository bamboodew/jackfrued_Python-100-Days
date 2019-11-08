'''
Created on 2019年8月29日
完全数（Perfect number），又称完美数或完备数，是一些特殊的自然数。
它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身。
如果一个数恰好等于它的因子之和，则称该数为“完全数”。第一个完全数是6，第二个完全数是28，第三个完全数是496，后面的完全数还有8128、33550336等等。
@author: jinshuang1
'''
# 约数：能被整除的数
from math import sqrt

# for PerfectNum in range(2, 1000):
#     for i in range(2, PerfectNum - 1):
#         if PerfectNum % i == 0:
#             s += i
#             print(s)
#     if s == PerfectNum:
#         print('完美数：%d' % PerfectNum)

for p in range(2, 1000):  # (a,b)表示a到b-1
    s = 1
    for i in range(2, int(sqrt(p)) + 1):  # 减少循环次数
        if p % i == 0:
#             print('%d ' % i, end='')
            if sqrt(p) != int(sqrt(p)):
                s += (i + p / i)
            else:
                s += (i + p / i) - sqrt(p)
#     print()
    if s == p:
        print(int(s))  

