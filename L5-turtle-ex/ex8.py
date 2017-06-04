'''
Write a program to draw a face of a clock that looks something like this:

http://openbookproject.net/thinkcs/python/english3e/_images/tess_clock1.png
'''

import turtle

t=turtle.Turtle()
t.shape("turtle")
t.color("red")

for i in range(12):
    t.penup()
    t.left(360/12*i)
    t.forward(100)
    t.pendown()
    t.forward(10)
    t.penup()
    t.forward(20)
    t.stamp()
    t.penup()
    t.home()

turtle.exitonclick()
