from person import IPerson

class Proffessor(IPerson):

    def __init__(self):
        self.name = "Proffesor"
    
    def speak(self):
        print("This is just a professor who happens to be a person too.")