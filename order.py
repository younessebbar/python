def display_info(person, status = "single"):
    print(f"person is: {person}")
    print(f"status is: {status}")

# Non defualt argument follows default arguement
# we can't do this

def display_info(person,  *args ,status = "single", **kwargs):
    print(f"person is: {person}")
    print(f"status is: {status}")
    print(f"args is: {args}")
    print(f"kwargs is: {kwargs}")

# *args tuple , kwargs -> (keyword arguments) which is a disctionary of arguments passed to the function
display_info("Younes", 1, 2, 3, 4, 5, 6, 7, status="single", age= 28, mood= "always sad", favMovie= "space odyssey", favSeries= "True detective S1")

def add_twice(val, lst= []):
    lst.append(val)
    lst.append(val)
    return lst

# this behaviour is weird, so the lst variable appends the values and doesn't start with an empty list each function call

add_twice(2)
# this call returns [2, 2]
add_twice(4)
# the catch is here, the second time the function gets called it returns this [2, 2, 4, 4]
#  to solve this problem we should do a workaround

def add_thrice(val, lst = None):
    if lst is None:
        lst = []
    lst.append(val)
    lst.append(val)
    lst.append(val)
    return lst

# this problem only involves mutable objects being used as default arguments, tuples won't have this problem

# unpacking arguments
def average(*args):
    total = 0
    for arg in args:
        total += arg
    return total / len(args)

nums = [4, 5, 78, 9, 12, 15, 4, 45]
# average(nums) this call won't work -> gives error because *args expects a number of arguments not a list
# solution

average(*nums)