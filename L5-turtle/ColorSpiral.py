import turtle
t = turtle.Turtle()
t.speed(0)
sides = 4
colors = ["red", "blue", "orange", "green", "yellow", "purple"]
turtle.bgcolor("black")
for i in range(300):
    t.pencolor(colors[i%sides])
    t.forward(i)
    t.left(360/sides+1)


