"""
Python 3.9.X and above is required

Factory Adapter Pattern

Decide during runtime the specific objects Client wants and create them dynamically.
Allows the interface of an existing class to be used as another interface.
Make existing classes work with others without modifying their source code.

"""

from person_factory import PersonFactory

user_choice = input("\nWhich type of person do you want to create ?\n1)Student\n2)Professor\n3)Assistant Professor\n\n").lower()
person = PersonFactory.create_person(user_choice)

try:    
    person.speak()
except AttributeError:
    print("Oops! Wrong 'Person' type. Please choose one of the above.")