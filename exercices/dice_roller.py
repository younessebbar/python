# My Humble solution to the exercice
from random import randint;

num_dice = int(input("How many dice are we rolling ? "))
num_sides = int(input("How many sides on each die ? "))

while True:
    result = "|"
    for die in range(num_dice):
        rand = randint(1, num_sides)
        result += f"{rand}|";
    print(result)
    result = ""
    roll_again = input("Roll again? (q to quit) ")
    if roll_again.lower() == "q":
        break



