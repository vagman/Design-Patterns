# Python 3.9.X and above is required

from error_logger import ErrorLogger
from registration import UserRegistration
from verification import Verification
from datetime import datetime

firstname = input("Enter firstname: ")
lastname = input("Enter lastname: ")
username = input("Enter username: ")
password = input("Enter password: ")
conf_password = input("Reenter password: ")



if password == conf_password:
    registration = UserRegistration(1, firstname, lastname, username, password)
    print(registration.register_user())

    if unauthorized == True:
        email = input("Enter email: ")
        verification = Verification(registration.firstname, email)
        print(verification.send_verification_email())

else:
    if not firstname or not lastname or not username or not password or not conf_password:
        timestamp = datetime.now()
        now = datetime.now()
        print(now.strftime("%m/%d/%Y, %H:%M:%S"))
        error = ErrorLogger(404, timestamp)
        print(error.error_logger(404))
