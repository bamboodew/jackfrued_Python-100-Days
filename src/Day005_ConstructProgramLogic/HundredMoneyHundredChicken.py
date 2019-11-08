'''
Created on 2019年8月29日
我国古代数学家张丘建在《算经》一书中提出的数学问题：鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
@author: jinshuang1
'''

# cock，hen，chick
for num_cock in range(1, 20):
#     num_hen = int((100 - 5 * num_cock) / 3)
#     print('%d %d' % (num_cock, num_hen))
    for num_hen in range(1, int((100 - 5 * num_cock) / 3) + 1):
        num_chick = (100 - 5 * num_cock - 3 * num_hen) * 3
        if num_cock + num_hen + num_chick == 100:
            print('母鸡%d只，公鸡%d只，雏鸡%d只' % (num_cock, num_hen, num_chick))
