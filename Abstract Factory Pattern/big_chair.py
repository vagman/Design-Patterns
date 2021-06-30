from ichair import IChair

class BigChair(IChair):
    
    def __init__(self):
        self.height = 80
        self.width = 80
        self.depth = 80

    def get_dimensions(self):
        return {"height": self.height, "width": self.width, "depth": self.depth}