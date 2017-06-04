import turtle
t = turtle.Turtle()
t.speed(0)
while True:
    num = int(input("How many sides?"))
    if num == 0:
        break
    if num == -1:
        t.clear()
    else:
        for i in range(num):
            for j in range(num):
                t.forward(50)
                t.left(360/num)
            t.left(360/num)
