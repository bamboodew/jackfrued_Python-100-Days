'''
Created on 2019年8月28日
输入半径计算圆的周长和面积

@author: jinshuang1
'''
import math

radius = float(input("请输入圆的半径："))
perimeter = 2 * math.pi * radius
area = math.pi * radius ** 2
print('周长：%.2f' % perimeter)
print('面积：%.2f' % area)
