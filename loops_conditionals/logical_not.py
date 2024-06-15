year = input("what year we you born in ? ")

if not year.isnumeric():
    year = input("That isn't a number. Try again please! what year were you born in ? ")

year = int(year)
print(f"You were born {2024 - year } years ago")