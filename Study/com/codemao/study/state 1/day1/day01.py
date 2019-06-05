import turtle
import random

pen = turtle.Pen()

# 开始进入Python的世界
turtle.bgcolor("#000000")
pen.pencolor("#ffff66")
pen.fillcolor("#ffff66")
pen.speed(100)
for __count in range(100):
    pen.penup()
    pen.goto(random.randint((-600), 600), random.randint((-350), 350))
    pen.pendown()
    size = random.randint(1, 50)
    pen.begin_fill()
    for __count in range(5):
        pen.forward(size)
        pen.left(144)
    pen.end_fill()
