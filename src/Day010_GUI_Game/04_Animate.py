import pygame

"""
说到动画这个词大家都不会陌生，事实上要实现动画效果，
本身的原理也非常简单，就是将不连续的图片连续的播放，
只要每秒钟达到了一定的帧数，那么就可以做出比较流畅的动画效果。
如果要让上面代码中的小球动起来，可以将小球的位置用变量来表示，
并在循环中修改小球的位置再刷新整个窗口即可。
"""


def main():
    # 初始化导入的pygame中的模块
    pygame.init()
    # 初始化用于显示的窗口并设置其大小
    screen = pygame.display.set_mode((800, 600))
    # 设置当前窗口的标题
    pygame.display.set_caption('大球吃小球')
    # 定义变量来表示小球在屏幕上的位置
    x, y = 50, 50

    running = True
    # 开启一个事件循环处理发生的事件
    while running:
        # 从消息列队中获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # 设置窗口的背景色
        screen.fill((242, 242, 242))
        # 绘制一个圆（参数分别是：屏幕、颜色、圆心位置、半径，0表示填充圆）
        pygame.draw.circle(screen, (255, 0, 0), (x, y), 30, 0)
        # 刷新当前窗口（渲染窗口将绘制的图形呈现出来）
        pygame.display.flip()  # 窗口一开始是黑色，会闪烁一下到fill的颜色
        # 每隔50ms就改变小球的位置再刷新窗口
        pygame.time.delay(100)
        x, y = x + 50, y + 50


if __name__ == '__main__':
    main()
