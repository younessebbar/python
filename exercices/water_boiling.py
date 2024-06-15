unit = input("What unit are you using ? ")
temp = int(input("What temperature is the water ? "))


if unit == "c":
    if temp >= 100:
        print("WATER IS BOILING!")
    else:
        print("WATER IS NOT BOILING, MUST HIT 100 CELSIUS")
elif unit == "f":
    if temp >= 212:
        print("WATER IS BOILING")
    else:
        print("WATER IS NOT BOILING MUST HIT 212 FAHRENHEIT")
else:
    if temp >= 373:
        print("WATER IS BOILING")
    else:
        print("WATER IS NOT BOILING MUST HIT 373 KELVIN")