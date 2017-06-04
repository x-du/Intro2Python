import turtle
t = turtle.Turtle()
t.speed(0)
num = int(turtle.numinput("Number of circles?", "How many circles?"))
turtle.bgcolor("black")
t.color("red")
for i in range(num):
    t.circle(100)
    t.left(360/num)

t.color("green")
for i in range(num):
    for j in range(4):
        t.forward(50)
        t.left(90)
    t.left(360/num)

turtle.exitonclick()
