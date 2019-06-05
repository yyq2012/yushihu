# # 在窗口中绘图
#
# 可以通过pygame中draw模块的函数在窗口上绘图，
# 可以绘制的图形包括：线条、矩形、多边形、圆、椭圆、圆弧等。
# 需要说明的是，屏幕坐标系是将屏幕左上角设置为坐标原点`(0, 0)`，
# 向右是x轴的正向，向下是y轴的正向，在表示位置或者设置尺寸的时候，
# 我们默认的单位都是[像素](https://zh.wikipedia.org/wiki/%E5%83%8F%E7%B4%A0)。
# 所谓像素就是屏幕上的一个点，
# 你可以用浏览图片的软件试着将一张图片放大若干倍，
# 就可以看到这些点。
# pygame中表示颜色用的是色光[三原色](https://zh.wikipedia.org/wiki/%E5%8E%9F%E8%89%B2)表示法，
# 即通过一个元组或列表来指定颜色的RGB值，
# 每个值都在0~255之间，因为是每种原色都用一个8位（bit）的值来表示，
# 三种颜色相当于一共由24位构成，这也就是常说的“24位颜色表示法”。

import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption('画圆')
    # 设置窗口的背景色
    screen.fill((242, 242, 242))
    # 绘制一个圆(参数分别是: 屏幕, 颜色, 圆心位置, 半径, 0表示填充圆)
    pygame.draw.circle(screen, (255, 0, 0), (100, 100), 30, 0)
    # 刷新当前窗口(渲染窗口将绘制的图像呈现出来)
    pygame.display.flip()
    running = True
    # 开启一个事件循环处理的事件
    while running:
        # 从消息队列中获取事件并进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
    main()