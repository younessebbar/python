from copy import copy
class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self):
        return f"Human named  {self.first} {self.last} aged {self.age}"
    
    def __len__(self):
        return self.age
    
    def __add__(self, other):
        if isinstance(other, Human):
            return Human(first="NewBorn", last=self.last, age=0)
        raise TypeError("Cannot add something that is not Human")
    
    def __mul__(self, other):
        if isinstance(other, int):
            return [copy(self) for i in range(0, other)]
        else:
            raise TypeError("Cannot multiply Human by non integer")


    
j = Human("Jennifer", "Aniston", 50)
k = Human("Kyle", "Jones", 42)
print(j)
print(len(j))
n = j + k
print(n)  
triplets = j * 3
triplets[0].first = "Bob"
triplets[1].first = "Rose"
triplets[2].first = "Samira"
print(triplets)