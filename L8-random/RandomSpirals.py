import turtle
import random

t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)
colors = ["red", "green", "yellow", "purple", "blue", "orange"]
for n in range(100):
    t.penup()
    x = random.randint(-300,300)
    y = random.randint(-400,400)
    t.setx(x)
    t.sety(y)
    t.color(random.choice(colors))
    size = random.randint(10,200)
    t.pendown()
    for i in range(size):
        t.forward(i)
        t.left(91)
