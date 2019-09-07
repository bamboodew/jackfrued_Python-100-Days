import time
from random import sample


def main():
    list0 = [x for x in range(1, 31)]
    # print(list0)
    L = []
    while len(list0) > 15:
        L += [list0[8]]
        list0 = list0[9:] + list0[:8]
        # print(list0)
    L.sort()
    list0.sort()
    print('非基督徒位置:', L)
    print('基督徒的位置:', list0)
    print()


if __name__ == '__main__':
    main()
