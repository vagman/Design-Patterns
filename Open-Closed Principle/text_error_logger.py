from datetime import datetime
from error_logger import ErrorLogger

class TextErrorLogger(ErrorLogger):
    
    def error_processor(self):
        err_msg=  "From OCP.py program:\nError performed while performing calculations. Please check your inputs and retry.\nTime: {}\n---------------".format(datetime.now())
        with open("logs.txt", "a") as writer:
            writer.write(err_msg + "\n\n")