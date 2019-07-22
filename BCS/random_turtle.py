from turtle import Turtle, done
from random import randint

# Create the sprite
leo = Turtle(shape='turtle')

# Setup the pen
leo.color('green')
leo.pendown()
leo.speed(0)

x = 5
for i in range(30):
    leo.setheading((x % 4) * 90)
    for j in range(10):
        leo.forward(x)
        leo.right(randint(-10, 10))
    x += 1

done()
