import turtle
t = turtle.Turtle()
s = turtle.Screen()

def drawSquare(x, y):
    t.penup()
    t.goto(x,y)
    for i in range(4):
        t.forward(50)
        t.left(90)

s.onClick(drawSquare,1)
s.listen()
