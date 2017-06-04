import turtle
t = turtle.Turtle()
t.speed(0)
colors = ["red", "blue", "orange", "green"]
for i in range(100):
    t.pencolor(colors[i%4])
    t.forward(i)
    t.left(91)


