from random import randrange, randint, sample


def display(balls):
    """
    输出列表中的双色球号码
    """
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print('%02d' % ball, end=' ')
    print()


def random_select():
    """
    随机选择一组号码
    """
    red_balls = [x for x in range(1, 34)]
    selected_balls = []
    selected_balls = sample(red_balls, 6)  # 使用random模块的sample函数来实现从列表中选择不重复的n个元素。
    selected_balls.sort()  # 按大小顺序排列
    selected_balls.append(randint(1, 16))  # 增加一个随机蓝色球
    return selected_balls


def main():
    n = int(input('机选几注: '))
    for _ in range(n):  # 循环n次
        display(random_select())


if __name__ == '__main__':
    main()
