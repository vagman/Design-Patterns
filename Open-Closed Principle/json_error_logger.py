import json
from error_logger import ErrorLogger

class JsonErrorLogger(ErrorLogger):
    
    def error_processor(self, error_data, filename, filepath):
        path = "./" + filepath + "/" + filename + ".json"
        with open(path, "w") as f:
            json.dump(error_data, f)

    error_data =  {
        "program": "OCP.py", 
        "code": "503", 
        "error_info": "Please check your input and try again." 
    }