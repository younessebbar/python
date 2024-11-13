class Animal:
    def speak(self):
        raise NotImplementedError("Subclass need to implement this method")

class Dog(Animal):
    def speak(self):
        return "WOOF"

class Cat(Animal):
    def speak(self):
        return "MEOW"

class Fish(Animal):
   pass

d = Dog()
print(d.speak())
f = Fish()
print(f.speak())
