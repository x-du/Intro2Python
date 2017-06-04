import turtle

turtle.setup(400,500)                # Determine the window size
s = turtle.Screen()                 # Get a reference to the window
s.title("Handling keypresses!")     # Change the window title
s.bgcolor("lightgreen")             # Set the background color
t = turtle.Turtle()               # Create our favorite turtle

# The next four functions are our "event handlers".
def h1():
   t.forward(30)

def h2():
   t.left(45)

def h3():
   t.right(45)

def h4():
    s.bye()                        # Close down the turtle window

# These lines "wire up" keypresses to the handlers we've defined.
s.onkey(h1, "Up")
s.onkey(h2, "Left")
s.onkey(h3, "Right")
s.onkey(h4, "q")

# Now we need to tell the window to start listening for events,
# If any of the keys that we're monitoring is pressed, its
# handler will be called.
s.listen()
#wn.mainloop()
