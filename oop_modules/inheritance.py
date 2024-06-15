class User:
    def __init__(self, name):
        print("Inside the user constructor")
        self.name = name
    
    def login(self):
        print(f"{self.name} Logged in!!")

class Admin(User):
    def __init__(self, name, permissions):
        print("Inside the constructor of admin")
        super().__init__(name)
        self.permissions = permissions


    def deleteUser(self ,username):
        print(f"{username} deleted successfully!")

class Moderator(User):
    def owner_of(self, departement):
        print(f"{self.name} is currently handling the {departement}, please check with them for more info.")

