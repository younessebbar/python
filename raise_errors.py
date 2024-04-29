def get_username():
    inp = input("Please enter your name: ")
    if not inp.isalpha():
        raise ValueError("Name can only contain alphabets")
    return inp

#  try/except
try:
    num = int(input("Enter a number: "))
except ValueError:
   print("Oh no, that isn't a number!")
except EOFError:
    print("You didn't enter anything")
except KeyboardInterrupt:
    print("Oops you interrupted the script")

print(f"You entered {num}")