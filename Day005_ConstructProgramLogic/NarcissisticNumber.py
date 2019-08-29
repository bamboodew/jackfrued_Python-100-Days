'''
Created on 2019年8月29日
水仙花数（Narcissistic number）也被称为超完全数字不变数（pluperfect digital invariant, PPDI）、
自恋数、自幂数、阿姆斯壮数或阿姆斯特朗数（Armstrong number），
水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身（例如：1^3 + 5^3+ 3^3 = 153）。
@author: jinshuang1
'''

# 目标三位数为abc，a为[1,9]，b和C为[0,9]
for a in range(1, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            if a ** 3 + b ** 3 + c ** 3 == a * 100 + b * 10 + c:
                NarcissisticNumber = a * 100 + b * 10 + c
                print('水仙花数：%d' % NarcissisticNumber)

# 水仙花数：153
# 水仙花数：370
# 水仙花数：371
# 水仙花数：407
