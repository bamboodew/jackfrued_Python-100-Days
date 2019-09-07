import time
from random import sample


def isElementRepeated(list0):
    if len(list0) == len(set(list0)):
        return 1  # 无重复
    else:
        return 0  # 有重复


def creatList_9_9():
    L0 = [x for x in range(1, 10)]
    # print(L0)
    List_9_9 = []  # sample表示随机取多个元素组成数列

    # 第0行
    List_9_9 += [sample(L0, 9)]
    print('第0行:', List_9_9[0])

    # 第1行
    L1 = sample(L0, 9)
    # print(L0)
    list_1 = List_9_9[0][0:3] + L1[0:3]
    list_2 = List_9_9[0][3:6] + L1[3:6]
    list_3 = List_9_9[0][6:] + L1[6:]

    while isElementRepeated(list_1) * isElementRepeated(list_2) * isElementRepeated(list_3) == 0:
        L1 = sample(L0, 9)
        list_1 = List_9_9[0][0:3] + L1[0:3]
        list_2 = List_9_9[0][3:6] + L1[3:6]
        list_3 = List_9_9[0][6:] + L1[6:]
        # print(L1)

    List_9_9 += [L1]
    print('第1行:', List_9_9[1])

    # 第2行
    L2 = sample(L0, 9)
    # print(L0)
    list_1 = List_9_9[0][0:3] + List_9_9[1][0:3] + L2[0:3]
    list_2 = List_9_9[0][3:6] + List_9_9[1][3:6] + L2[3:6]
    list_3 = List_9_9[0][6:] + List_9_9[1][6:] + L2[6:]

    list_col = []
    columnRepeated = 1
    for i in range(9):
        list_col = [List_9_9[0][i]] + [List_9_9[1][i]] + [L2[i]]
        if isElementRepeated(list_col) == 0:
            columnRepeated = 0
            break

    while isElementRepeated(list_1) * isElementRepeated(list_2) * isElementRepeated(list_3) * columnRepeated == 0:
        L2 = sample(L0, 9)

        columnRepeated = 1
        for i in range(9):
            list_col = [List_9_9[0][i]] + [List_9_9[1][i]] + [L2[i]]
            if isElementRepeated(list_col) == 0:
                columnRepeated = 0
                break

        list_1 = List_9_9[0][0:3] + List_9_9[1][0:3] + L2[0:3]
        list_2 = List_9_9[0][3:6] + List_9_9[1][3:6] + L2[3:6]
        list_3 = List_9_9[0][6:] + List_9_9[1][6:] + L2[6:]
        # print(L2)

    List_9_9 += [L2]
    print('第2行:', List_9_9[2])

    # 第3行
    L3 = sample(L0, 9)

    list_col = []
    columnRepeated = 1
    for i in range(9):
        list_col = [List_9_9[0][i]] + [List_9_9[1][i]] + [List_9_9[2][i]] + [L3[i]]
        if isElementRepeated(list_col) == 0:
            columnRepeated = 0
            break
    while columnRepeated == 0:
        L3 = sample(L0, 9)

        columnRepeated = 1
        for i in range(9):
            list_col = [List_9_9[0][i]] + [List_9_9[1][i]] + [List_9_9[2][i]] + [L3[i]]
            if isElementRepeated(list_col) == 0:
                columnRepeated = 0
                break
    List_9_9 += [L3]
    print('第3行:', List_9_9[3])

    # 第4行
    L4 = sample(L0, 9)
    # print(L0)
    list_1 = List_9_9[3][0:3] + L4[0:3]
    list_2 = List_9_9[3][3:6] + L4[3:6]
    list_3 = List_9_9[3][6:] + L4[6:]

    list_col = []
    columnRepeated = 1
    for i in range(9):
        list_col = [List_9_9[0][i]] + [List_9_9[1][i]] + [List_9_9[2][i]] + [List_9_9[3][i]] + [L4[i]]
        if isElementRepeated(list_col) == 0:
            columnRepeated = 0
            break
    # ElementRepeated_9 = 1
    # for j in range(3):
    #     L_3_4 = [List_9_9[0][3 * j]] + [List_9_9[1][3 * j]] + [List_9_9[2][3 * j]] + [L3[3 * j]] + [L3[3 * j + 1]] + [
    #         L3[3 * j + 2]] + [L4[3 * j]] + [L4[3 * j + 1]] + [L4[3 * j + 2]]
    #     if isElementRepeated(L_3_4) == 1:
    #         ElementRepeated_9 = 0  # 9个元素不重复就终端循环
    #         break

    while isElementRepeated(list_1) * isElementRepeated(list_2) * isElementRepeated(list_3) * columnRepeated == 0:
        L4 = sample(L0, 9)
        # print(L4)
        list_1 = List_9_9[3][0:3] + L4[0:3]
        list_2 = List_9_9[3][3:6] + L4[3:6]
        list_3 = List_9_9[3][6:] + L4[6:]
        # list_col = []
        columnRepeated = 1
        for i in range(9):
            list_col = [List_9_9[0][i]] + [List_9_9[1][i]] + [List_9_9[2][i]] + [List_9_9[3][i]] + [L4[i]]
            if isElementRepeated(list_col) == 0:
                columnRepeated = 0
                break
        # ElementRepeated_9 = 1
        # for j in range(3):
        #     L_3_4 = [List_9_9[0][3 * j]] + [List_9_9[1][3 * j]] + [List_9_9[2][3 * j]] + [L3[3 * j]] + [
        #         L3[3 * j + 1]] + [L3[3 * j + 2]] + [L4[3 * j]] + [L4[3 * j + 1]] + [L4[3 * j + 2]]
        #     if isElementRepeated(L_3_4) == 1:
        #         ElementRepeated_9 = 0  # 9个元素不重复就终端循环
        #         # print(L_3_4)
        #         break
        # # continue

    List_9_9 += [L4]
    # print(List_9_9[4])

    # 第5行
    L5 = sample(L0, 9)
    # print(L5)
    # print()
    # print(L0)
    list_1 = List_9_9[3][0:3] + List_9_9[4][0:3] + L5[0:3]
    list_2 = List_9_9[3][3:6] + List_9_9[4][3:6] + L5[3:6]
    list_3 = List_9_9[3][6:] + List_9_9[4][6:] + L5[6:]

    list_col = []
    columnRepeated = 1
    for i in range(9):  # 列循环
        list_col = [List_9_9[0][i]] + [List_9_9[1][i]] + [List_9_9[2][i]] + [List_9_9[3][i]] + [List_9_9[4][i]] + [
            L5[i]]
        if isElementRepeated(list_col) == 0:
            columnRepeated = 0
            break

    n = 0
    while isElementRepeated(list_1) * isElementRepeated(list_2) * isElementRepeated(list_3) * columnRepeated == 0:
        n += 1

        if n > 10000:
            # print('n > 1000')
            del List_9_9[4]

            # 重新生成第4行
            L4 = sample(L0, 9)
            # print(L0)
            list_1 = List_9_9[3][0:3] + L4[0:3]
            list_2 = List_9_9[3][3:6] + L4[3:6]
            list_3 = List_9_9[3][6:] + L4[6:]

            list_col = []
            columnRepeated = 1
            for i in range(9):
                list_col = [List_9_9[0][i]] + [List_9_9[1][i]] + [List_9_9[2][i]] + [List_9_9[3][i]] + [L4[i]]
                if isElementRepeated(list_col) == 0:
                    columnRepeated = 0
                    break
            while isElementRepeated(list_1) * isElementRepeated(list_2) * isElementRepeated(
                    list_3) * columnRepeated == 0:
                L4 = sample(L0, 9)
                list_1 = List_9_9[3][0:3] + L4[0:3]
                list_2 = List_9_9[3][3:6] + L4[3:6]
                list_3 = List_9_9[3][6:] + L4[6:]
                list_col = []
                columnRepeated = 1
                for i in range(9):
                    list_col = [List_9_9[0][i]] + [List_9_9[1][i]] + [List_9_9[2][i]] + [List_9_9[3][i]] + [L4[i]]
                    if isElementRepeated(list_col) == 0:
                        columnRepeated = 0
                        break

            List_9_9 += [L4]
            # print(List_9_9[4])
            n = 0  # n清零

        # 重新生成第5行
        # print('重新生成第5行:', n)

        L5 = sample(L0, 9)
        # print(L5)
        list_1 = List_9_9[3][0:3] + List_9_9[4][0:3] + L5[0:3]
        list_2 = List_9_9[3][3:6] + List_9_9[4][3:6] + L5[3:6]
        list_3 = List_9_9[3][6:] + List_9_9[4][6:] + L5[6:]

        list_col = []
        columnRepeated = 1
        for i in range(9):
            list_col = [List_9_9[0][i]] + [List_9_9[1][i]] + [List_9_9[2][i]] + [List_9_9[3][i]] + [
                List_9_9[4][i]] + [L5[i]]
            if isElementRepeated(list_col) == 0:
                columnRepeated = 0
                break

    List_9_9 += [L5]
    print('第4行:', List_9_9[4])
    print('第5行:', List_9_9[5])

    # 第6行
    L6 = sample(L0, 9)

    list_col = []
    columnRepeated = 1
    for i in range(9):
        list_col = [List_9_9[0][i]] + [List_9_9[1][i]] + [List_9_9[2][i]] + [List_9_9[3][i]] + [List_9_9[4][i]] + [
            List_9_9[5][i]] + [L6[i]]
        if isElementRepeated(list_col) == 0:
            columnRepeated = 0
            break

    while columnRepeated == 0:
        L6 = sample(L0, 9)
        list_col = []
        columnRepeated = 1
        for i in range(9):
            list_col = [List_9_9[0][i]] + [List_9_9[1][i]] + [List_9_9[2][i]] + [List_9_9[3][i]] + [List_9_9[4][i]] + [
                List_9_9[5][i]] + [L6[i]]
            if isElementRepeated(list_col) == 0:
                columnRepeated = 0
                break

    List_9_9 += [L6]
    # print('第6行:', List_9_9[6])

    # 第7行
    L7 = sample(L0, 9)
    list_1 = List_9_9[6][0:3] + L7[0:3]
    list_2 = List_9_9[6][3:6] + L7[3:6]
    list_3 = List_9_9[6][6:] + L7[6:]

    list_col = []
    columnRepeated = 1
    for i in range(9):
        list_col = [List_9_9[0][i]] + [List_9_9[1][i]] + [List_9_9[2][i]] + [List_9_9[3][i]] + [List_9_9[4][i]] + [
            List_9_9[5][i]] + [List_9_9[6][i]] + [L7[i]]
        if isElementRepeated(list_col) == 0:
            columnRepeated = 0
            break
        # print(columnRepeated)

    n = 0
    while isElementRepeated(list_1) * isElementRepeated(list_2) * isElementRepeated(list_3) * columnRepeated == 0:
        n += 1
        # print(n)
        if n > 10000:
            # print('n > 1000')
            del List_9_9[6]

            # 重新生成第6行
            L6 = sample(L0, 9)

            list_col = []
            columnRepeated = 1
            for i in range(9):
                list_col = [List_9_9[0][i]] + [List_9_9[1][i]] + [List_9_9[2][i]] + [List_9_9[3][i]] + [
                    List_9_9[4][i]] + [List_9_9[5][i]] + [L6[i]]
                if isElementRepeated(list_col) == 0:
                    columnRepeated = 0
                    break

            while columnRepeated == 0:
                L6 = sample(L0, 9)
                list_col = []
                columnRepeated = 1
                for i in range(9):
                    list_col = [List_9_9[0][i]] + [List_9_9[1][i]] + [List_9_9[2][i]] + [List_9_9[3][i]] + [
                        List_9_9[4][i]] + [List_9_9[5][i]] + [L6[i]]
                    if isElementRepeated(list_col) == 0:
                        columnRepeated = 0
                        break

            List_9_9 += [L6]
            # print(List_9_9[6])
            n = 0  # n清零

        L7 = sample(L0, 9)
        list_1 = List_9_9[6][0:3] + L7[0:3]
        list_2 = List_9_9[6][3:6] + L7[3:6]
        list_3 = List_9_9[6][6:] + L7[6:]

        list_col = []
        columnRepeated = 1  # 重置为1，避免受前面代码的影响
        for i in range(9):
            list_col = [List_9_9[0][i]] + [List_9_9[1][i]] + [List_9_9[2][i]] + [List_9_9[3][i]] + [List_9_9[4][i]] + [
                List_9_9[5][i]] + [List_9_9[6][i]] + [L7[i]]
            if isElementRepeated(list_col) == 0:
                columnRepeated = 0
                break

    List_9_9 += [L7]
    print('第6行:', List_9_9[6])
    print('第7行:', List_9_9[7])

    # 第8行
    L8 = []
    list_col = []
    for j in range(9):
        list_col = [List_9_9[0][j]] + [List_9_9[1][j]] + [List_9_9[2][j]] + [List_9_9[3][j]] + [List_9_9[4][j]] + [
            List_9_9[5][j]] + [List_9_9[6][j]] + [List_9_9[7][j]]
        L8 += [x for x in L0 if x not in list_col]
    # print(L8)

    List_9_9 += [L8]
    print('第8行:', List_9_9[8])


def main():
    n = 0
    while True:
        start = time.time()
        creatList_9_9()
        stop = time.time()
        print()

        n += 1
        print('第%d次：%.2fs' % (n, (stop - start)))
        print()


if __name__ == '__main__':
    main()
