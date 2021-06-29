from datetime import date, datetime
from payment_processor import PaymentProcessor
from client import Client
from datetime import datetime

class Payment(PaymentProcessor):

    def __init__(self):
        self.payment_time = datetime.now()
    
    def get_payment_time(self):
        return self.payment_time

    def payment(self, client: Client, payment_service = "paypal"):
        if (payment_service == "paypal"):
            print("\nClient with username {} made a payment with {}.".format(client.get_username(), payment_service))
        # If payment is from Stripe:
            # Do something else..