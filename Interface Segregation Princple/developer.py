from employee import Employee

class Developer(Employee):
    
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def get_salary(self):
        return self.salary

    def working_time(self, hours):
        return 5 * hours + 2
    
    def calculate_salary(self, working_time) -> int:
        # Working_time * $/hour
        return working_time * 4
    
    def break_time(self):
        return 5