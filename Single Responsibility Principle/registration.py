class UserRegistration:

    def __init__(self, user_id: int, firstname: str, lastname: str, username: str, password: str):
        self.__user_id = user_id
        self.__firstname = firstname
        self.__lastname = lastname
        self.__username = username
        self.__password = password

    def get_use_id(self):
        return self.__user_id

    def set_user_id(self, user_id):
        self.__user_id = user_id

    def get_firstname(self):
        return self.__firstname

    def set_firstname(self, firstname):
        self.__firstname = firstname

    def get_lastname(self):
        return self.__lastname

    def set_lastname(self, lastname):
        self.__lastname = lastname

    def get_username(self):
        return self.__username

    def set_username(self, username):
        self.__username = username

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

    def register_user(self) -> str:
        # Send data to DataBase..
        return "\nUser {} with ID {} has been added to the database successfully!".format(self.__firstname, self.__user_id)