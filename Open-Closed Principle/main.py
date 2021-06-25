"""
Python 3.9.X and above is required

Open-Closed Principle

''Software entities (classes, modules, functions) should be open for extension and closed for Modifications.'' ~ Dr. Bertrand Meyer 1988
In our example adding new functionality for a new error type will not require changing any existing function. 
Implemented with: Strategy Design Pattern
"""

from event_error_logger import EventErrorLogger
from text_error_logger import TextErrorLogger
from json_error_logger import JsonErrorLogger

try:
    a = int(input("Enter an integer value A: "))
    b = int(input("Enter an integer value B: "))
    calculation = a / b
    print("{} / {} = {}".format(a, b, calculation))

except ZeroDivisionError:
    event_error_logger = EventErrorLogger()
    text_error_logger = TextErrorLogger()
    json_error_logger = JsonErrorLogger()

    text_error_logger.error_processor()
    event_error_logger.error_processor()
    json_error_logger.error_processor(json_error_logger.error_data, "logs", "/")