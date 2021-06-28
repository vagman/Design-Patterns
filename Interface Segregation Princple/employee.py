from abc import abstractmethod
from work import Work

# Abstract class 'Employee' as it doesn't implement all the methods of its superclass
class Employee(Work):

    @abstractmethod
    def break_time(self):
        pass