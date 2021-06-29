from abc import ABC, abstractmethod
from client import Client

class PaymentProcessor(ABC):

    @abstractmethod
    def payment(self, client: Client, payment_service: str):
        raise NotImplementedError
