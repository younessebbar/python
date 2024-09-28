def colorize(text, color):
    colors = ("red", "blue","green","yellow","orange", "teal", "purple")
    if type(color) is not str:
        raise TypeError("Color must be an instance of str")
    elif color not in colors:
        raise ValueError("Invalid color choice")
    print(f"Printed {text} in {color}")

# Try except 
# try:
#     younes
# except NameError as err:
#     print("You tried to use a variable that was never created")

# print("After the execpt")

d = {"name": "Rick"}

def get(d, key):
    try:
        return d[key]
    except KeyError as err:
        print("You tried accessing a key that doesn't exist:", err)

get(d, "city")
