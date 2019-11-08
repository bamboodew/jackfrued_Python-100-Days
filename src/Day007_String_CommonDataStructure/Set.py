def main():
    set1 = {1, 2, 3, 3, 3, 2}
    print('set1:', set1)
    print('Length =', len(set1))

    set2 = set(range(1, 10))
    print(set2)

    set1.add(4)
    set1.add(5)
    set2.update([11, 12])  # 在集合中增加迭代
    print(set1, set2)
    set2.update([10])  # set都是自动从小排列的
    print(set2)

    set2.discard(5)  # 删除值为5的元素
    print(set2)

    if 4 in set2:
        set2.remove(4)
    print('set2:', set2)

    for elem in set2:
        print(elem ** 2, end=' ')
    print()

    set3 = set((1, 2, 3, 3, 2, 1))
    print(set3.pop())  # 抽出字典的第一个元素
    print(set3)
    print()

    print('set1:', set1)
    print('set2:', set2)
    print('set3:', set3)
    print()
    print(set1 & set2)
    print(set1 | set2)
    print(set1 - set2)
    print(set1 ^ set2)

    print(set2 <= set1)
    print(set3 <= set1)
    print(set1 >= set2)
    print(set1 >= set3)


if __name__ == '__main__':
    main()
