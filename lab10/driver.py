'''This file is to set up our output window and get everything set up in our solar system
Created Spring 2018
lab10
@author: Nana Osei Asiedu Yirenkyi (na29)'''

#gains access to the turtle and solar_system code
import turtle
from solar_system import *

window = turtle.Screen() #Name the screen where the turtle will appear "window"
window.setworldcoordinates(-1, -1, 1, 1)

#Prompts user for the values of a user defined planet
user_planet = input('Enter the name of a planet:')
radius = float(input('\nEnter the radius of the planet:'))
mass = float(input('\nEnter the mass of the planet:'))
dist = float(input('\nEnter the distance from the sun:'))
color = input('\nEnter the color of the planet:')

#creates a solar system object and add the sun, and planets
ss = Solar_System()
ss.add_sun(Sun("SUN", 8.5, 1000, 5800))
ss.add_planet(Planet("EARTH", .475, 5000, 0.6, 'blue'))
ss.add_planet(Planet(user_planet, radius, mass, dist, color))

# Keep the window open until it is clicked
window.exitonclick()