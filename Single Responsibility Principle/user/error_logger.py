class ErrorLogger:

    def __init__(self, error_code: int, timestamp: str):
        self.errorCode = error_code
        self.timestamp = timestamp

    def error_logger(self, error_code) -> str:
        if error_code == 200:
            return "200 - OK"
        elif error_code == 404:
            return "404 - Not Found"
        elif error_code == 401:
            return "401 - Unauthorized"
        else: 
            return "500 - Internal Server Error" 