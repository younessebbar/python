# color  = input("enter a color: ")
# if color:
#     print(f"{color} is my favorite color too!")

#NOT
#AND
#OR

# num_lives = 9
# if num_lives:
#     print(f"YOU HAVE {num_lives} LIVES LEFT")
# else:
#     print("GAME OVER, OUT OF LIVES")

# Veterans get in free on tuesdays
# Infants under 2 get in for free always
day = "Tuesday"
is_veteran = True
age = 43

# if age <= 2 or day == "Tuesday" and is_veteran:
#     print("YOU GET IN FOR FREE TODAY!")
# else:
#     print("SORRY YOU HAVE TO PAY")

if not (age <= 2 or day == "Tuesday" and is_veteran):
    print("SORRY YOU HAVE TO PAY")
