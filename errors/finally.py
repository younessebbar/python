# try:
# except:
# else: will run when except does not
# finally: will run no matter what
while True:
    try:
        num = int(input("Please enter a number: "))
    except:
        print("That's not a number!")
    else:
        print("Good job, you entered a number!")
        break
    finally:
        print("RUNS NO MATTER WHAT!")

def divide(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        print("don't divide by zero please!")
    except TypeError as err:
        print("a and b must be ints or floats!")
        print(err)
    else:
        print(f"{a} divided by {b} is: {result}")

