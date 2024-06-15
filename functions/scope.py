# Global scope example
animal = "Cat"

print("OUTISIDE OF FUNCTION: ", animal)

def func():
    print("INSIDE FUNC: ", animal)
    def inner_func():
        print("INSIDE INNER_FUNC: ", animal)
    inner_func()

func()

# Local scope example

def cube(num):
    answer = num ** 3
    print(answer)

cube(3)

# Scope in loops and conditionals ? 

for char in "SPIDERMAN":
    color = "magenta"
    name = "Peter parker"
    print(char)

print("AFTER LOOP", color, name)

# Enclosing scope
def outer():
    animal = "Nudibranches"
    def inner():
        animal = "Echidna"
        print("INSIDE INNER FUNCTION: ", animal)
    inner()

outer()

# Global variables

def outer():
    global animal
    animal = "Spider crab"
    
outer()
print(animal)