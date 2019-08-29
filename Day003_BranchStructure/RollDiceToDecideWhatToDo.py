'''
Created on 2019年8月28日
掷骰子决定做什么事情
@author: jinshuang1
'''
from random import randint

face = randint(1, 6)

if face == 1:
    result = 'Sing A Song'
elif face == 2:
    result = 'Dance'
elif face == 3:
    result = 'Bark'
elif face == 4:
    result = 'Push-ups'
elif face == 5:
    result = 'Tongue Twister'
else:
    result = 'Cold Jokes'
print('%d对应的动作是%s' % (face, result))
