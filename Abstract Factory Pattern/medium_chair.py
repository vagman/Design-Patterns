from ichair import IChair

class MediumChair(IChair):
    
    def __init__(self):
        self.height = 70
        self.width = 70
        self.depth = 70

    def get_dimensions(self):
        return {"height": self.height, "width": self.width, "depth": self.depth}