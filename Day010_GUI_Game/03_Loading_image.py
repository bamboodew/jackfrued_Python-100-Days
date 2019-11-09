import pygame

"""
如果需要直接加载图像到窗口上，
可以使用pygame中image模块的函数来加载图像，
再通过之前获得的窗口对象的blit方法渲染图像，
代码如下所示。
"""


def main():
    # 初始化导入的pygame中的模块
    pygame.init()
    # 初始化用于显示的窗口并设置其大小
    screen = pygame.display.set_mode((800, 600))
    # 设置当前窗口的标题
    pygame.display.set_caption('大球吃小球')
    # 设置窗口的背景色
    screen.fill((242, 242, 242))
    # 通过指定的文件名加载图像
    ball_image = pygame.image.load('./res/ball.png')  # .代表相对路径，与当前程序在同一路径之下
    # 在窗口上渲染图像
    screen.blit(ball_image, (400, 300))

    # 刷新当前窗口（渲染窗口将绘制的图形呈现出来）
    pygame.display.flip()  # 窗口一开始是黑色，会闪烁一下到fill的颜色
    running = True
    # 开启一个事件循环处理发生的事件
    while running:
        # 从消息列队中获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
    main()
