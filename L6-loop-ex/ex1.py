import turtle
t = turtle.Turtle()
t.color("pink")
t.pensize(3)
x = -200
y = 0

t.penup()
t.goto(x,y)
for i in range(5):
    t.pendown()
    for j in range(4):
        t.forward(20)
        t.left(90)
    t.penup()
    x = x+ 40
    t.goto(x,y)

turtle.exitonclick()
