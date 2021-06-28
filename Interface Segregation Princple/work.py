from abc import ABC, abstractmethod

class Work(ABC):

    @abstractmethod
    def working_time(self) -> int:
        raise NotImplementedError
    
    @abstractmethod
    def break_time(self) -> int:
        raise NotImplementedError