import time
from random import sample


#
#
# def creatList_top(List_, i, j):
#     list_top = []
#     for _ in range(i):
#         list_top += [List_[_][j]]
#     return list_top
#
#
# def creatList_left(List_, j):  # j为列标:0~8；一维数组
#     list_left = []
#
#     if j > 0:
#         for _ in range(j):
#             list_left += List_[:j]
#     return list_left
#
#
# def creatList_3_3(List_, i, j):  # j为列标:0~8；一维数组
#     list_3_3 = []
#
#     if i % 3 != 0:
#         for m in range(i - i % 3, i):
#             for n in range(j - j % 3, j + 2 - j % 3 + 1):
#                 list_3_3 += [List_[m][n]]
#
#     return list_3_3


def main():
    L0 = [x for x in range(1, 10)]
    # print(L0)
    List_9_9 = []  # sample表示随机取多个元素组成数列

    # 第0行
    List_9_9 += [sample(L0, 9)]

    # 第1行
    L0 = [sample(L0, 9)]
    if List_9_9[0][0:3] + List_9_9[0][0:3]:
        print(List_9_9[0])  # 换行打印二维数组
    #
    # # 第1行
    # List_9_9 += [[]]
    # for i in range(3):
    #     List_9_9[1] += sample([x for x in List_9_9[0][3:] if x not in List_9_9[1]], 1)
    # for i in range(3):
    #     L_ = [x for x in List_9_9[0][6:] if x not in List_9_9[1]]
    #     L_345 = sample([x for x in List_9_9[0][0:3] if x not in List_9_9[1]], 3 - i - len(L_)) + L_
    #     List_9_9[1] += sample(L_345, 1)
    # for _ in range(3):
    #     List_9_9[1] += sample([x for x in List_9_9[0][0:6] if x not in List_9_9[1]], 1)
    #     # print(List_9_9[1])
    #
    # # print(List_9_9[1])  # 换行打印二维数组
    # print()
    # # time.sleep(1)
    #
    # # 第2行
    # List_9_9 += [[]]
    # for i in range(3):
    #     for j in range(3):
    #         L2 = List_9_9[0][i * 3:i * 3 + 3] + List_9_9[1][i * 3:min(i * 3 + 3, 8)] + List_9_9[2]
    #         List_9_9[2] += sample([x for x in L0 if x not in L2], 1)
    #
    # # 第3行
    # List_9_9 += [[]]
    # for i in range(8):
    #     L30 = List_9_9[0][i + 1:] + List_9_9[1][i + 1:] + List_9_9[2][i + 1:]
    #     L31 = List_9_9[0][i:i + 1] + List_9_9[1][i:i + 1] + List_9_9[2][i:i + 1] + List_9_9[3]
    #     while len(set(x for x in L30 if x not in L31)) > 8 - i:
    #         list0 = sample([x for x in L30 if x not in L31], 1)
    #
    #     List_9_9[3] += sample([x for x in L30 if x not in L31], 1)
    # #     print(List_9_9[3])
    #
    # # for i in range(8):
    # #     L3 = List_9_9[0][i:i + 1] + List_9_9[1][i:i + 1] + List_9_9[2][i:i + 1] + List_9_9[3]  # 可与第0行合并
    # #     List_9_9[3] += sample([x for x in L0 if x not in L3], 1)
    # #
    # # L3 = List_9_9[0][8:] + List_9_9[1][8:] + List_9_9[2][8:] + List_9_9[3]  # 可与第0行合并
    # # List_9_9[3] += sample([x for x in L0 if x not in L3], 1)
    #
    # # print(List_9_9[3])
    #
    # # 第4行
    # # List_9_9 += [[]]
    # # # print(List_9_9[4])
    # # for i in range(3):
    # #     L4 = List_9_9[4] + List_9_9[0][i:i + 1] + List_9_9[1][i:i + 1] + List_9_9[2][i:i + 1]
    # #     List_9_9[4] += sample([x for x in List_9_9[3][3:] if x not in L4], 1)
    #
    # # for i in range(3):
    # #     L4 = List_9_9[4] + List_9_9[0][i + 3:i + 4] + List_9_9[1][i + 3:i + 4] + List_9_9[2][i + 3:i + 4]
    # #     L_ = [x for x in List_9_9[3][6:] if x not in L4]
    # #
    # #     L_345 = sample([x for x in List_9_9[3][0:3] if x not in L4], 3 - i - len(L_)) + L_
    # #     List_9_9[4] += sample(L_345, 1)
    #
    # # List_9_9[4] += sample([x for x in List_9_9[3][0:6] if x not in List_9_9[4]], 1)
    # # List_9_9[4] += sample([x for x in List_9_9[3][0:6] if x not in List_9_9[4]], 1)
    # # List_9_9[4] += sample([x for x in List_9_9[3][0:6] if x not in List_9_9[4]], 1)
    #
    # # for _ in range(3):
    # #     List_9_9[4] += sample([x for x in List_9_9[3][0:6] if x not in List_9_9[4]], 1)
    #
    # # print(List_9_9[3])

    for _ in range(len(List_9_9)):
        print(List_9_9[_])  # 换行打印二维数组


if __name__ == '__main__':
    main()
