import time


def main():
    list1 = []
    list1_len = int(input('请输入数列元素个数：'))
    for i in range(list1_len):
        list1.append(int(input('请输入第%d个元素：' % i)))

    print(list1)

    sumTwo = int(input('请输入和：'))
    for i in range(list1_len - 1):
        if sumTwo - list1[i] in list1[i + 1:]:
            print('第%d个数和第%d个数的和为%d' % (i, i + 1 + list1[i + 1:].index((sumTwo - list1[i])), sumTwo))


if __name__ == '__main__':
    main()
