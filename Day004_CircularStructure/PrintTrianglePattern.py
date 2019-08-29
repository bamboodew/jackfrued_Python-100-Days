'''
Created on 2019年8月28日
打印各种三角形图案

*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********
@author: jinshuang1
'''

row = int(input('请输入行数：'))
for i in range(row):
    for j in range(i + 1):
        print('*', end='')  # 给end赋值为空，就不会换行
    print()

for i in range(row):
    for j in range(row - 1 - i):
        print(' ', end='')
    for j in range(i + 1):
        print('*', end='')
    print()

for i in range(row):
    for j in range(row - 1 - i):
        print(' ', end='')
    for j in range(2 * i + 1):
        print('*', end='')
    print()
