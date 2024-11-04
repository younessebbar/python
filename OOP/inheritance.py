class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}"

    def make_sound(self, noise):
        return f"This animal says {noise}"


class Cat(Animal):
    def __init__(self, name, breed, toy):
       super().__init__(name, species="Cat")
       self.breed = breed
       self.toy = toy
    
    def play(self):
        return f"{self.name} plays with {self.toy}"
       
blue = Cat("Blue", "Turkish angora", "String")
print(blue)
print(blue.play())

class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        if age >= 0:
            self._age = age
        else:
            self._age = 0
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("Age can't be negative!!")
    
    @property
    def full_name(self):
        return f"{self.first} {self.last}"
    
    @full_name.setter
    def full_name(self, name):
        self.first, self.last = name.split(" ")
    

# jasmine = Human("Jasmine", "Kirou", 26)
# jasmine.age = 27
# jasmine.full_name = "Younes SEBBAR"
# print(jasmine.full_name)
# print(jasmine.__dict__)
