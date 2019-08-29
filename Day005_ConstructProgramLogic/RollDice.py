'''
Created on 2019年8月29日
掷骰子3个，三个之和的概率
@author: jinshuang1
'''
import random

for num in range(100, 1000, 100):  # 分别掷100次的整数次
    list_0 = [0] * 16
    probability = [0] * 16
    
#     sum_3, sum_4, sum_5, sum_6, sum_7, sum_8, sum_9, sum_10, sum_11, sum_12, sum_13, sum_14, sum_15, sum_16, sum_17, sum_18 = 0
    for i in range(0, num):
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        c = random.randint(1, 6)
        s = a + b + c
        list_0[s - 3] += 1
    for j in range(16):
        probability[j] = '%.1f%%' % (list_0[j] / num * 100)
#     print(list)
    print(probability)
