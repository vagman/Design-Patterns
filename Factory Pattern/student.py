from person import IPerson

class Student(IPerson):

    def __init__(self):
        self.name = "Student"

    def speak(self):
        print("This is just a student who happens to be a person too.")