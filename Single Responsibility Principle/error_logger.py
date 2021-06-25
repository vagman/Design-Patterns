from datetime import datetime

class ErrorLogger:

    def __init__(self, error_code: int):
        self.__error_code = error_code
        self.__timestamp = str(datetime.now())

    def get_error_code(self):
        return self.__error_code

    def set_error_code(self, error_code):
        self.__error_code = error_code

    def error_logger(self, error_code) -> str:
        if error_code == 200:
            return str(datetime.now()) + ": Error 200 - OK"
        elif error_code == 404:
            return str(datetime.now())  + ": Error 404 - Not Found"
        elif error_code == 401:
            return "Error 401 - Unauthorized"
        else: 
            return "Error 500 - Internal Server Error"
