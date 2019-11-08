'''
Created on 2019年8月28日
输入年份 如果是闰年输出True 否则输出False

@author: jinshuang1
'''

year = int(input('请输入年份：'))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('%d年是闰年' % year)
else :
    print('%d年不是闰年' % year)
