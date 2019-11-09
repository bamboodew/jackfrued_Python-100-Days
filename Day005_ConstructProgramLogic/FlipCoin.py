'''
Created on 2019年8月29日
求抛硬币的正反面概率
@author: jinshuang1
'''
import random

# num = int(input('请输入抛硬币的次数：'))
for num in range(1000, 100000, 1000):
    positive = 0  # 正面
    negative = 0  # 反面
    for i in range(0, num):
        result = random.randint(0, 1)
        if result == 0:
            negative += 1 
        else:
            positive += 1
    print('正面%d次，概率为%.2f%%；反面%d次，概率为%.2f%%' % (positive, positive / num * 100, negative, negative / num * 100))
