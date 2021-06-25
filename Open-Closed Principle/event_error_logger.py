from datetime import datetime
from error_logger import ErrorLogger

class EventErrorLogger(ErrorLogger):

    def error_processor(self):
        err_msg = "---------------\nFrom OCP.py program:\nError performed while performing calculations. Please check your inputs and retry.\nTime: {}\n---------------".format(datetime.now())
        print(err_msg)        