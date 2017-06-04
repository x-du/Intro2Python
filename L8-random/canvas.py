import turtle
s=turtle.Screen()
t=turtle.Turtle()
t.penup()
def gotoMouse(x,y):
    t.clear()
    t.goto(x,y)
    t.write("x="+str(int(t.xcor()))+", y="+str(int(t.ycor())),font=("Arial", 24, "normal"))

s.onclick(gotoMouse,1)
s.listen()
