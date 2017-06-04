
def drawBar(grade):
    if grade >=90:
        gradesLetter = "A"
    elif grade >=80:
        gradesLetter = "B"
    elif grade >=70:
        gradesLetter = "C"
    elif grade >=60:
        gradesLetter = "D"
    else:
        gradesLetter = "F"
    #t.color("red")
    t.begin_fill()
    t.forward(20)
    t.left(90)
    t.forward(grade)
    t.left(90)
    t.forward(20)
    t.write(" "+gradesLetter, font=("Arial", 14, "normal"))
    t.left(90)
    t.forward(grade)
    t.left(90)
    t.end_fill()


grades = [90, 100, 82, 70, 59, 61]

import turtle
t = turtle.Turtle()
t.color("blue","red")
t.penup()
t.goto(-200,0)
for grade in grades:
    t.pendown()
    drawBar(grade)
    t.penup()
    t.forward(40)

turtle.exitonclick()
