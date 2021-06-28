from employee import Employee

class Accountant(Employee):
    
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def working_time(self, hours):
        return 5 * hours - 5