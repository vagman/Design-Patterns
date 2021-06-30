from abc import ABC, abstractmethod

class IFurnitureFactory(ABC):

    @abstractmethod
    def get_furniture(furniture_type: str):
        pass