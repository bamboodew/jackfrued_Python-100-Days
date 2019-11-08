'''
Created on 2019年8月28日
英制单位与公制单位互换
@author: jinshuang1
'''

value = float(input('请输入长度：'))
unit = input('请输入单位：')
if unit == 'in' or unit == '英寸':
    print('%.2f英寸 = %.2f厘米' % (value, value * 2.54))
elif unit == 'cm' or unit == '厘米':
    print('%.2f厘米 = %.2f英寸' % (value, value / 2.54))
else:
    print('请输入有效的单位')
