# Handy rule of thumb, only import what you need
# All different way to import
# import random
# import random as omg_so_random
# from random import *
# from random import choice, shuffle, randint
from random import choice as pick, shuffle, randint as magic_number_chooser
from keyword import iskeyword
from termcolor import colored
import pyfiglet


msg = input("What text do you want to print ? ")
color = input("what color ? ")
valid_colors = ("black", "red", "green", "yellow",
                "blue", "magenta", "cyan", "white")

if color not in valid_colors:
    color = "magenta"
ascii_art = pyfiglet.figlet_format(msg)
colored_ascii = colored(ascii_art, color=color)
print(colored_ascii)

print(f"Hi my name is: {__name__}")


# fruits = ["Apple","Banana", "Strawberry", "Blackberry", "Oranges", "Peach"]
#  return random element from a sequence
# print(pick(fruits))

# print(magic_number_chooser(1, 100))

#  Shuffles the sequenece and returns none
# shuffle(fruits)
# print(fruits)

def contains_keyword(*strings):
    for word in strings:
        if iskeyword(word):
            return True
    return False

# text = colored("Hello world!",color="cyan", on_color="on_magenta" ,attrs=["blink"])
# print(text)
# cprint("Hello world!","red", "on_green")
