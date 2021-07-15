from abc import ABC, abstractmethod

class ErrorLogger(ABC):

    @abstractmethod
    def error_processor(self):
        pass