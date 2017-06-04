import turtle
import time

t = turtle.Turtle()
t.color("black", "blue")
t.begin_fill()
for i in range(4):
    t.forward(100)
    t.left(90)

t.end_fill()
time.sleep(10)
