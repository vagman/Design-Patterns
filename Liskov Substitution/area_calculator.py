from shape import Shape
from typing import List

class AreaCalculator:
    # Specify that we pass only type 'list' consisting of shape objects
    def calculateArea(self, shapes: List[Shape]):
        for shape in shapes:
            print("Area of the shape is: {}".format(shape.width * shape.height))