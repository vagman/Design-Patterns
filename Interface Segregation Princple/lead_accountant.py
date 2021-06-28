from employer import Employer

class LeadAccountant(Employer):
    
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def working_time(self, hours):
        return 5 * hours - 5

    def calculate_hired_people(self, resumes_received):
        return resumes_received - 1