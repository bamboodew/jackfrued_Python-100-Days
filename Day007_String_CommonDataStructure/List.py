def main():
    list1 = [1, 3, 5, 7, 100]
    print(list1)

    list2 = ['hello'] * 5
    print(list2)
    print(list2[2] == list2[3])  # True

    print(len(list1))
    print(list1[2])
    print(list1[-1])

    list1[2] = 300  # 修改列表元素
    print(list1)

    list1.append(400)  # 末尾添加元素
    print(list1)

    list1.insert(1, 200)  # 按索引添加元素
    print(list1)

    list1 += [1000, 2000]  # 末尾添加元素
    print(list1)

    list1.remove(3)  # 删除指定元素
    print(list1)

    del list1[0]
    print(list1)

    list1.clear()
    print(list1)


if __name__ == '__main__':
    main()
