import turtle
import random

t = turtle.Turtle()
t.speed(0)
colors = ["blue", "red", "yellow", "purple", "black", "pink"]

def drawSpiral(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(random.choice(colors))
    for i in range(100):
        t.forward(i)
        t.left(91)


turtle.onscreenclick(drawSpiral)
