# age = int(input("How old are you ? "))
# if(age <= 12):
#     print("Child ticket is 12$")
# elif(age >= 18):
#     print("Adult ticket is 15$")
# else:
#     print("Senior ticket is 20$")

# color = input("Choose your favorite Color ")
# if(color.lower() == "red"):
#     print("GOOD CHOICE!")
# elif(color.lower() == "blue"):
#     print("DECENT CHOICE!")
# else:
#     print("BAD CHOICE! :(")


# Name Length

first_name = input("What is your first name ? ")
last_name = input("What is your last name ? ")
name_length = len(first_name + last_name)

print("*" * 60)
if name_length > 12:
    print(f"{first_name} {last_name} is Longer than the average american name")
elif name_length == 12:
     print(f"{first_name} {last_name} is exactly the average american name")
else:
     print(f"{first_name} {last_name} is Shorter than the average american name")
     
print("*" * 60)