class User:
    active_users = 0

    @classmethod
    def display_active_users(cls):
       return f"There are currently {cls.active_users} active users!"
    
    @classmethod
    def from_string(cls, data_str):
        first,last, age = data_str.split(",")
        return cls(first, last, int(age))

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1
    
    def __repr__(self):
        user = dict(first= self.first, last= self.last, age= self.age)
        return str(user)
    
    def full_name(self):
        return f"{self.first} {self.last}"

    def logout(self):
       User.active_users -= 1
       return f"{self.first} has logged out"
    
    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."
    
    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th, birthday {self.first}"

user1 = User("Younes", "Sebbar", 28)
print(User.active_users)
user2 = User("Inas", "Laaroussi", 23)

# print(user1.full_name())
# print(user2.full_name())
print(user1.birthday())
print(User.active_users)

# print(user1.initials())
# print(user2.initials())
# print(user1.is_senior())
# print(user2.is_senior())


class Comment:
    def __init__(self, username, text, likes=0):
        self.username = username
        self.text = text
        self.likes = likes
        
c = Comment("davey123", "lol you're so silly", 3) 
another_comment = Comment("rosa77", "soooo cute!!!") 

class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0.0
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance


acct = BankAccount("Younes")
print(acct.owner) 
print(acct.balance)
print(acct.deposit(10))
print(acct.withdraw(3))  
print(acct.balance)