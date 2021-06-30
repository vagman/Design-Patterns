from ichair import IChair

class SmallChair(IChair):
    
    def __init__(self):
        self.height = 60
        self.width = 60
        self.depth = 60

    def get_dimensions(self):
        return {"height": self.height, "width": self.width, "depth": self.depth}