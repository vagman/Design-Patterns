from abc import abstractmethod
from work import Work

# Abstract class 'Employer' as it doesn't implement all the methods of its superclass
class Employer(Work):

    @abstractmethod
    def working_time(self):
        pass

    @abstractmethod
    def calculate_hired_people(self):
        pass