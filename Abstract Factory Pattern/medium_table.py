from itable import ITable

class MediumTable(ITable):

    def __init__(self):
        self.height = 170
        self.width = 170
        self.depth = 170

    def get_dimensions(self):
        return {"height": self.height, "width": self.width, "depth": self.depth}