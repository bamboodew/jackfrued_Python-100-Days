from random import randint

print(2 ** 10)

i = randint(0, 1000)
s = input("请输入：")
num = int(s)
# print(i)

while num != i:
    if num > i:
        print("大了\n")
    elif num < i:
        print("小了\n")
        
    s = input("请再输入：")
    num = int(s)

print("\n猜对了")
