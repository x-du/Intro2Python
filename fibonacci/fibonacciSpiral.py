import turtle
import random

t = turtle.Turtle()
f1 = 0*20
f2 = 1*20
x=0
y=0
turtle.colormode(255)
def drawSquare(x, y, size):

    t.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()
    t.penup()
    t.forward(size)
    t.left(90)
    t.pendown()
    t.color("black")
    t.circle(size,90)
    t.penup()
    t.circle(size,270)
    t.right(90)
    t.backward(size)
    t.pendown()

    
for i in range(10):
    drawSquare(x,y,f2)
    f = f1 + f2
    t.left(90)
    t.backward(f-f2)
    f1=f2
    f2=f

