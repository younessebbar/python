flavors = ["chocolate", "vanilla", "pistachio", "lemon", "strawberry"]
response = input("What flavor do you want ? ")

while response.lower() not in flavors:
    response = input("We currently do not have that flavor, please choose again: ")

print(f"One {response} ice cream is coming right up! ")