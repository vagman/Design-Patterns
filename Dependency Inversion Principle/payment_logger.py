from abc import ABC, abstractmethod
from payment import Payment

class PaymentLogger(ABC):
    
    @abstractmethod
    def log_payment(self, payment: Payment):
        pass