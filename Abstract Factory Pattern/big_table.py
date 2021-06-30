from itable import ITable

class BigTable(ITable):

    def __init__(self):
        self.height = 180
        self.width = 180
        self.depth = 180

    def get_dimensions(self):
        return {"height": self.height, "width": self.width, "depth": self.depth}