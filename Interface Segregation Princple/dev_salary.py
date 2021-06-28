from abc import ABC, abstractmethod

class DevSalary(ABC):

    def calculate_salary(working_time) -> int:
        raise NotImplementedError