"""
Python 3.9.X and above is required

Dependency Inversion Principle

Dependency should be on abstractions.
A. High-level modules should not depend upon low-level modules. Both should depend upon abstractions.
B. Abstractions should not depend on details. Details should depend upon abstractions.

If you consequently apply the Open/Closed Principle and the Liskov Substitution Principle to your code,
it will also follow the Dependency Inversion Principle. ~ Thorben Janssen

"""

from client import Client
from payment import Payment
from logger import Logger

# Initialize objects
client = Client("Jonathan")
payment = Payment()
logger = Logger()

# Perform client related actions based on abstract model classes
client.buy_bycycle()
payment.payment(client)
logger.log_payment(payment)