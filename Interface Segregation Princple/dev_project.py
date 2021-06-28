from abc import ABC, abstractmethod

class DevProject(ABC):
    
    def calculate_project_budget() -> int:
        raise NotImplementedError