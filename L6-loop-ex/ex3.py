import turtle
t = turtle.Turtle()
t.color("blue")
num = 20
for i in range(num):
    for j in range(4):
        t.forward(50)
        t.left(90)
    t.left(360/num)

turtle.exitonclick()
