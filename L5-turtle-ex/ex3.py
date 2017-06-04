'''
Use for loops to make a turtle draw these regular polygons (regular means all sides the same lengths, all angles the same):
An equilateral triangle
A square
A hexagon (six sides)
An octagon (eight sides)
'''

import turtle
import time
t = turtle.Turtle()

def draw(sides):
    for i in range(sides):
        t.forward(100)
        t.left(360/sides)

draw(3)
time.sleep(3)
t.clear()
t.home()
draw(4)
time.sleep(4)
t.clear()
t.home()
draw(6)
time.sleep(3)
t.clear()
t.home()
draw(8)
time.sleep(5)
