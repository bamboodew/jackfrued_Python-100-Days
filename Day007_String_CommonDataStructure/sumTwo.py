import time


def main():
    list1 = []
    list1_len = int(input('请输入数列元素个数：'))
    for i in range(list1_len):
        list1.append(int(input('请依次输入元素：')))

    print(list1)

    sumTwo = int(input('请输入和：'))
    for i in range(list1_len - 1):
        if sumTwo - list1[i] in list1[i + 1:]:
            print([i, i + 1 + list1[i + 1:].index((sumTwo - list1[i]))])


if __name__ == '__main__':
    main()
