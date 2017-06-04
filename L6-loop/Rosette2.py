import turtle
t = turtle.Turtle()

num = 8
for i in range(num):
    t.circle(100)
    t.left(360/num)


turtle.exitonclick()
