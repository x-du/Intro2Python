v = input("Do you want spiral? (yes or no)")
if v == "yes":

    import turtle
    t = turtle.Turtle()
    t.speed(0)
    for x in range(100):
        t.forward(2*x)
        t.left(91)
    turtle.exitonclick()

print("Ok, we are done!")
