from abc import ABC, abstractmethod

class ITable(ABC):

    @abstractmethod
    def get_dimensions():
        pass