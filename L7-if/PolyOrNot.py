import turtle
t = turtle.Turtle()
t.speed(0)
num = 8
answer = input("Ploygon or Circle? p/c:")
if answer == "c":
    for i in range(num):
        t.circle(50)
        t.left(360/num)
else:
    for i in range(num):
        for j in range(num):
            t.forward(100)
            t.left(360/num)
        t.left(360/num)

turtle.exitonclick()
