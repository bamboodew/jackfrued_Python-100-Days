'''
Created on 2019年8月29日
规则：玩家掷两个骰子，每个骰子点数为1-6，如果第一次点数和为7或11，则玩家胜；如果点数和为2、3或12，则玩家输庄家胜。
若和为其他点数，则记录第一次的点数和，玩家继续掷骰子，直至点数和等于第一次掷出的点数和则玩家胜；若掷出的点数和为7则庄家胜。
@author: jinshuang1
'''
import random

print('每一轮10元，共有本金100元；第1轮：7、11玩家胜，2、3、12庄家胜')

money = 100
i = 1
while money > 0:
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    if a + b == 7 or a + b == 11:
        print('第%d轮玩家胜：%d+%d=%d' % (i, a, b, a + b))
        money += 10
        print('剩余本金%d' % money)
        i += 1
    elif a + b == 2 or a + b == 3 or a + b == 8 or a + b == 6:
        print('第%d轮庄家胜：%d+%d=%d' % (i, a, b, a + b))
        money -= 10
        print('剩余本金%d' % money)
        i += 1
    else:
        print('第%d轮无胜负：%d+%d=%d' % (i, a, b, a + b))
        s = a + b
        i += 1
        while 1:
            a = random.randint(1, 6)
            b = random.randint(1, 6)
            if a + b == s:
                print('第%d轮玩家胜：%d+%d=%d' % (i, a, b, a + b))
                money += 10
                print('剩余本金%d' % money)
                i += 1
                break
            elif a + b == 7:
                print('第%d轮庄家胜：%d+%d=%d' % (i, a, b, a + b))
                money -= 10
                print('剩余本金%d' % money)
                i += 1
                break
            else:
                print('第%d轮无胜负：%d+%d=%d' % (i, a, b, a + b))
                i += 1
                continue
