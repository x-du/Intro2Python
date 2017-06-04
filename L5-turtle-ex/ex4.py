'''
A drunk pirate makes a random turn and then takes 100 steps forward, makes another random turn, takes another 100 steps, turns another random amount, etc. A social science student records the angle of each turn before the next 100 steps are taken. Her experimental data is [160, -43, 270, -97, -43, 200, -940, 17, -86]. (Positive angles are counter-clockwise.) Use a turtle to draw the path taken by our drunk friend.
'''

import turtle
pirate = turtle.Turtle()

turns = [160, -43, 270, -97, -43, 200, -940, 17, -86]

for i in turns:

    pirate.setheading(pirate.heading()+i)
    print(pirate.heading())
    pirate.forward(100)

turtle.exitonclick()
