from registration import UserRegistration

class Verification:
    
    def __init__(self, firstname: str, email: str):
        self.__firstname = firstname
        self.__email = email

    def send_verification_email(self) -> str:
        # If Error Logger didn't find any errors...
        return "\nVerification email has been sent to {} with email: {}".format(self.__firstname, self.__email)