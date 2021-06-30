from abc import ABC, abstractmethod

class IChair(ABC):

    @abstractmethod
    def get_dimensions():
        pass