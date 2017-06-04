import turtle
import random

t = turtle.Turtle()
t.speed(0)
turtle.colormode(255)
#colors = ["blue", "red", "yellow", "purple", "black", "pink"]

drawing = False
def drawSpiral(x, y):
    global drawing
    if not drawing:
        drawing = True
        t.penup()
        t.goto(x, y)
        t.pendown()
        color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

        t.color(color)
        for i in range(100):
            t.forward(i)
            t.left(91)
        drawing = False

turtle.onscreenclick(drawSpiral)
