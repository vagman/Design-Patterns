from employer import Employer
from dev_project import DevProject

class LeadDeveloper(Employer, DevProject):

    def working_time(self, hours) -> int:
        return 5 * hours + 2

    def calculate_hired_people(self, resumes_received) -> int:
        return resumes_received - 5
    
    def calculate_project_budget(working_time) -> int:
        # Formula: working_time * hours per day * months
        return working_time * 8 * 3