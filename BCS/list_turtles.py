from turtle import Turtle, done
from random import randint

# Create list of turtles
my_turtles = []

# Populate the list
# One turtle for each colour
for c in ['red', 'green', 'blue']:
    t = Turtle(shape='turtle')
    t.color(c)
    t.pendown()
    my_turtles.append(t)

# Execute a number of animations steps
for i in range(100):
    # Work through each turtle
    # taking a step
    for t in my_turtles:
        t.forward(5)
        t.right(randint(-100, 100))

done()
