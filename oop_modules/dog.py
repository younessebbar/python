class Dog:
    species = 'canine'
    num_dogs = 0

    def __init__(self, name, breed, location) -> None:
        self.name = name
        self.breed = breed
        self.location = location
        self.tricks = []
        self.available = True
        Dog.num_dogs += 1

    @classmethod
    def register_stray(cls):
        return cls("coming soon", "unknown", "unknown")

    def learn_trick(self, new_trick):
        if new_trick not in self.tricks:
            self.tricks.append(new_trick)

    def bark(self):
        print(f"{self.name} says WOOF!")
    
    def perform_trick(self, trick):
        if trick in self.tricks:
            print(f"{self.name} performs {trick}")
        else:
            print(f"{self.name} doesn't know how to do {trick}")

elton = Dog("Elton", "Mutt", 45230)
elton.learn_trick("sit")
elton.learn_trick("roll")
elton.learn_trick("down")

shaia = Dog("Shaia", "Husky", 41230)
shaia.learn_trick("sit")
shaia.perform_trick("sit")
