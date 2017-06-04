import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.listen()
t.speed(0)
turtle.bgcolor("black")
t.color("yellow")

s.onclick(t.goto)

s.onkey(t.penup, "u")
s.onkey(t.pendown, "d")

def moveLeft():
    t.setx(t.xcor()-10)

def moveRight():
    t.setx(t.xcor()+10)

def moveUp():
    t.sety(t.ycor()+10)

def moveDown():
    t.sety(t.ycor()-10)


s.onkey(moveUp, "Up")
s.onkey(moveDown, "Down")
s.onkey(moveLeft, "Left")
s.onkey(moveRight, "Right")

def drawSpiral(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for i in range(100):
        t.circle(i)
        t.left(91)

s.onclick(drawSpiral, 2)

s.onkey(t.clear, "c")

def red():
    t.color("red")
def green():
    t.color("green")
def blue():
    t.color("blue")

s.onkey(red,"R")
s.onkey(green,"G")
s.onkey(blue, "B")

def increaseWidth():
    if t.width()<20:
        t.width(t.width()+1)
def decreaseWidth():
    if t.width()>1:
        t.width(t.width()-1)
