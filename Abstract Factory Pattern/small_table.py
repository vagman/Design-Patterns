from itable import ITable

class SmallTable(ITable):

    def __init__(self):
        self.height = 160
        self.width = 160
        self.depth = 160

    def get_dimensions(self):
        return {"height": self.height, "width": self.width, "depth": self.depth}