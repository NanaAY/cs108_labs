'''A program for drawing a line with tuples
Lab 03
@author: Toby Sterk (ths6)
@author: Nana Osei (na29)
'''

# Import necessary items
import turtle
import math

# Give the name "window" to the screen where the turtle will appear.
window = turtle.Screen()

# Create a turtle and name it bob.
bob = turtle.Turtle()

# Prompt user for x1, y1, x2, y2
x1 = float(input("Please enter the first x value: "))
y1 = float(input("Please enter the first y value: "))
x2 = float(input("Please enter the second x value: "))
y2 = float(input("Please enter the second y value: "))

# Create tuples for first and last point
point1 = (x1, y1)
point2 = (x2, y2)

# Hide the arrowhead
bob.hideturtle()

# Move Bob to the first point
bob.goto(point1)


# Describe the first point with italic Arial size 20
point1_str = 'p1 '+ str(point1)
bob.write(point1_str,font = ('Arial',20,'italic' ))

# Draw a line from the first point to the second
bob.goto(point2)

# Describe the second point
point2_str = 'p2 '+ str(point2)
bob.write(point2_str,font = ('Arial',20,'italic' ))

# Keep the window open until it is clicked.
window.exitonclick()