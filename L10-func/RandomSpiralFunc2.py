import turtle
import random

t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)
colors = ["red", "green", "yellow", "purple", "blue", "orange"]
def drawRandomSpiral(x, y, color):
    t.penup()
    t.setx(x)
    t.sety(y)
    t.color(color)
    size = random.randint(10,200)
    t.pendown()
    for i in range(size):
        t.forward(i)
        t.left(91)

for i in range(30):
    x = random.randint(-300,300)
    y = random.randint(-400,400)
    color = random.choice(colors)
    drawRandomSpiral(x, y, color)
