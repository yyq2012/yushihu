# # 使用Pygame进行游戏开发
#
# Pygame是一个开源的Python模块，专门用于多媒体应用（如电子游戏）的开发，
# 其中包含对图像、声音、视频、事件、碰撞等的支持。
# Pygame建立在[SDL](https://zh.wikipedia.org/wiki/SDL)的基础上，
# SDL是一套跨平台的多媒体开发库，用C语言实现，被广泛的应用于游戏、模拟器、
# 播放器等的开发。而Pygame让游戏开发者不再被底层语言束缚，
# 可以更多的关注游戏的功能和逻辑。
#
# 下面我们来完成一个简单的小游戏，
# 游戏的名字叫“大球吃小球”，当然完成这个游戏并不是重点，
# 学会使用Pygame也不是重点，最重要的我们要在这个过程中体会如何使用前面讲解的面向对象程序设计，
# 学会用这种编程思想去解决现实中的问题。

import pygame


def main():
    # 初始化导入pygame 中的模块
    pygame.init()
    # 初始化用于显示的窗口和大小
    screen = pygame.display.set_mode((800, 600))
    # 设置窗口的标题
    pygame.display.set_caption('大球吃小球')
    running = True
    # 开启一个事件循环处理的事件
    while running:
        # 从消息队列中获取消息并处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
    main()
