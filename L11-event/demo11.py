import turtle
t = turtle.Turtle()
s = turtle.Screen()
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
    t.goto(x, y)
    for i in range(100):
        t.forward(i)
        t.left(91)

s.onclick(drawSpiral, 2)
s.listen()
