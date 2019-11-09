from enum import Enum, unique
from math import sqrt
from random import randint

import pygame


@unique
class Color(Enum):
    """颜色"""
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (242, 242, 242)

    @staticmethod
    def random_color():
        """获得随机颜色"""
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return r, g, b


class Ball(object):
    """球"""

    def __init__(self, x, y, radius, sx, sy, color=Color.RED):
        """初始化方法"""
        self.x = x
        self.y = y
        self.radius = radius
        self.sx = sx
        self.sy = sy
        self.color = color
        self.alive = True

    def move(self, screen):
        """移动"""
        self.x += self.sx
        self.y += self.sy
        if self.x - self.radius <= 0 or \
                self.x + self.radius >= screen.get_width():  # 超出屏幕左侧或右侧时
            self.sx = -self.sx  # 反向运动
        if self.y - self.radius <= 0 or \
                self.y + self.radius >= screen.get_height():  # 超出屏幕顶部或底部
            self.sy = -self.sy  # 反向运动

    def eat(self, other):
        """吃其他球"""
        if self.alive and other.alive and self != other:
            dx, dy = self.x - other.x, self.y - other.y
            distance = sqrt(dx ** 2 + dy ** 2)
            if distance < self.radius + other.radius \
                    and self.radius > other.radius:
                other.alive = False
                self.radius = self.radius + int(other.radius * 0.146)

    def draw(self, screen):
        """在窗口上绘制球"""
        pygame.draw.circle(screen, self.color,
                           (self.x, self.y), self.radius, 0)


def main():
    # 定义用来装球的容器
    balls = []
    # 初始化导入的pygame中的模块
    pygame.init()
    # 初始化用于显示的窗口并设置窗口的大小
    screen = pygame.display.set_mode((800, 600))
    # 设置当前窗口的标题
    pygame.display.set_caption('大球吃小球')
    running = True  # 初始化running的值

    # 开启一个循环，处理发生的事件
    while running:
        # 从消息列队中获取事件并对其进行处理
        for event in pygame.event.get():  # 消息列队：pygame.event.get()
            if event.type == pygame.QUIT:  # 卸载
                running = False  # 停止运行

            # 处理鼠标事件：点击1次
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # 获得点击鼠标的位置
                x, y = event.pos
                radius = randint(5, 50)  # 随机半径10~100
                sx, sy = randint(-5, 5), randint(-5, 5)  # 随机移动速度，每次-10~10之间
                color = Color.random_color()  # 随机颜色
                # 在点击鼠标的位置创建一个球（实例）
                ball = Ball(x, y, radius, sx, sy, color)
                # 将球添加到容器中
                balls.append(ball)
        # 屏幕填充为白色
        screen.fill((255, 255, 255))
        # 取出容器中的球
        for ball in balls:
            if ball.alive:
                ball.draw(screen)  # 如果没被吃掉就绘制
            else:
                balls.remove(ball)  # 否则就移除

        # 刷新当前窗口（渲染窗口将绘制的图形呈现出来）
        pygame.display.flip()  # 窗口一开始是黑色，会闪烁一下到fill的颜色

        # 每隔50ms改变球的位置并刷新窗口
        pygame.time.delay(10)  # 每次间隔的时间，越短就越快
        for ball in balls:
            pass
            ball.move(screen)
            # 检查球有没有吃到其他的球
            for other in balls:
                pass
                # ball.eat(other)


if __name__ == '__main__':
    main()
