from payment_logger import PaymentLogger
from payment import Payment
from datetime import datetime

class Logger(PaymentLogger):

    def log_payment(self, payment: Payment):
            log_message = "Succesful payment at {}.\nTime: {}\n---------------".format(payment.get_payment_time() ,datetime.now())
            with open("payments.txt", "a") as writer:
                writer.write(log_message + "\n\n")