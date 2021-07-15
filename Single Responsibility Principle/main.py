"""
Python 3.9.X and above is required

Single Responsibility Principle

A class should have only one job. 
If a class has more than one responsibility, it becomes coupled. 
A change to one responsibility results to modification of the other responsibility.
"""

from error_logger import ErrorLogger
from registration import UserRegistration
from verification import Verification
from random import randint

firstname = input("Enter firstname: ")
lastname = input("Enter lastname: ")
username = input("Enter username: ")
password = input("Enter password: ")
conf_password = input("Reenter password: ")

if not firstname or not lastname or not username or not password or not conf_password: 
    
    error = ErrorLogger(401)
    print(error.error_logger(401))
else:
    if password == conf_password:
        
        if randint(0, 1):
            email = input("Enter email: ")
            registration = UserRegistration(1, firstname, lastname, username, password)
            verification = Verification(registration.get_firstname(), email)
            print(registration.register_user())
            print(verification.send_verification_email())

        else:
            error = ErrorLogger(404)
            print(error.error_logger(404))
    else: 
        print("\nOops! Passwords do not match. Exiting the program..")