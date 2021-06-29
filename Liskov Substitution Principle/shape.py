class Shape:

    def __init__(self):
        self.shape_name = ""
        self._width = 0
        self._height = 0

    def get_width(self):
        return self._width

    def set_width(self, width_value):
        self._height = width_value

    def get_height(self):
        return self._width

    def set_height(self, height_value):
        self._height = height_value

    width = property(get_width, set_width)
    height = property(get_height, set_height)