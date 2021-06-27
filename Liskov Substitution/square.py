from shape import Shape

class Square(Shape):
    
    def __init__(self):
        self._width = 0
        self._height = 0

    def get_width(self):
        return self._width

    def set_width(self, width_value):
        if ((width_value != self._height) and (self._wdth != 0)):
            raise Exception("Invalid width and height for Sqaure shape.\nINFO: Width and height can't be diffrent.")
        else:
            self._width = width_value
            self._height = width_value

    def get_height(self):
        return self._height

    def set_height(self, height_value):
        if ((height_value != self._width) and (self._height != 0)):
            raise Exception("Invalid width and height for Sqaure shape.\nINFO: Width and height can't be diffrent.")
        else:
            self._width = height_value
            self._height = height_value
            
    width = property(get_width, set_width)
    height = property(get_height, set_height)