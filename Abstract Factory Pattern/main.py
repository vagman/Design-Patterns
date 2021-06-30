"""
Python 3.9.X and above is required

Abstract Factory Adapter Pattern

Same as Factory Pattern but now we have factories that create diffrent factory types.
Abstract factory method is a good practice to produce similar type of many objects
"""

from furniture_factory import FurnitureFactory

furniture0 = FurnitureFactory.get_furniture("BigChair")
print("\n{} : {}\n".format(furniture0.__class__, furniture0.get_dimensions()))

furniture1 = FurnitureFactory.get_furniture("SmallChair")
print("{} : {}\n".format(furniture1.__class__, furniture1.get_dimensions()))

furniture2 = FurnitureFactory.get_furniture("MediumTable")
print("{} : {}\n".format(furniture2.__class__, furniture2.get_dimensions()))