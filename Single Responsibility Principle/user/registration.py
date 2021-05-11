class UserRegistration:

    def __init__(self, userID: int, firstname: str, lastname: str, username: str, password: str):
        self.userID = userID 
        self.firstname = firstname
        self.lasstname = lastname
        self.username = username
        self.password = password
    
    def getUserID():
        return self.userID

    def setUserID():
        self.userID = userID
    
    def getFirstname():
        return self.firstname
    
    def setFirstname():
        self.firstname = firstname

    def getLastname():
        return self.lasstname
    
    def setLastname():
        self.lastname = lastname

    def getUsername():
        return self.username

    def setUserID():
        self.userID = userID

    def getPassword():
        return self.password
    
    def register_user(self) -> str:
        return "User {} with ID {} has been added to the database successfully!".format(self.firstname, self.userID)
    
