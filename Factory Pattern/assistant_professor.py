from person import IPerson

class AssistantProffessor(IPerson):

    def __init__(self):
        self.name = "Assistant Professor"
    
    def speak(self):
        print("This is just an assistant professor who happens to be a person too.")