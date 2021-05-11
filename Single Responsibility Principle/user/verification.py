class Verification:
    
    def __init__(self, firstname, email):
        self.firstname = firstname
        self.email = email

    def send_verification_email(self):
        # If Error Logger didn't find any errors...
        return "Verification email has been sent to the user with email: {}".format(self.email)


