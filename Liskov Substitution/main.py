"""
Liskov Substitution Principle

A sub-class must be substitutable for its super-class.
The aim of this principle is to ascertain that a sub-class can assume the place of its super-class without errors. 
If the code finds itself checking the type of class then, it mhas violated this principle.

"""

from area_calculator import AreaCalculator
from square import Square
from rectangle import Rectangle
from box import Box

# Square example
square = Square()
square.height = 10

# Rectangle example
rectangle = Rectangle()
rectangle.width = 10
rectangle.height = 5

# Create a new shape that doesnt inherit Shape class
box = Box(10, 20)

# Add shapes to list
shapes = [square, rectangle, box]

# Use area calculator for all the diffrent shapes we created
ac = AreaCalculator()
ac.calculateArea(shapes)