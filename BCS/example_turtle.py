from turtle import Turtle, done

# First ask user for some guidance
# Do this before creating any turtles
my_colour = input('Please enter the pen colour: ')

# Create the sprite
leo = Turtle(shape='turtle')

# Setup the pen
leo.color(my_colour)
leo.pendown()
leo.speed(0)

x = 5
for i in range(10):
    leo.setheading((x % 4) * 90)
    for j in range(36):
        leo.forward(x)
        leo.right(10)
    x += 1

done()
