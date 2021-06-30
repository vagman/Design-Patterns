from student import Student
from professor import Proffessor
from assistant_professor import AssistantProffessor

class PersonFactory:

    @staticmethod
    def create_person(person_type):
        if (person_type == "student"):
            return Student()
        if (person_type == "professor"):
            return Proffessor()
        if (person_type == "assistant professor"):
            return AssistantProffessor()
        