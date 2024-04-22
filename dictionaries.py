prices = {
    "arugala": 11,
    "basil": 25,
    "blackberries": 50,
    "blueberries": 30,
    "coconut": 75,
    "fennel": 37,
    "strawberry": 13
}

product = input("what are you buying ? ")

while not product in prices:
    product = input("we currently do not have that product, please try again: ")
    
price = prices[product]
print(f"{product} is {price} MAD")

# dict.pop(key) removes the key, value pair and returns the value
# dict.popitem(), remove the most recently added key-value pair, it returns the item as a tuple
# dict.clear(), deletes all items from dictionary. it returns none
# we can also use del to remove items from dictionary, returns none