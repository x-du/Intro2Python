import turtle
t = turtle.Turtle()
t.color("pink")
t.pensize(3)
x = 0
y = 0
w = 20

t.penup()

for i in range(5):
    t.pendown()
    for j in range(4):
        t.forward(w)
        t.left(90)
    t.penup()
    x = x -20
    y = y -20
    w = w + 40
    t.goto(x,y)

turtle.exitonclick()
