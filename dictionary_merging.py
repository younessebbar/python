dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"d": 4, "e": 5, "f": 6, "a": "dunkin donuts"}

# update merges 2 dictionary, in this case a with the value dunkin donuts is going to replace the a with value 1
# dict1.update(dict2)

# we can use ** to combine multiple dictionary into a new dictionary (dictionary unpacking)
dict3 = { **dict1, **dict2 }
# dict3 in this case is going to have the key-value pairs of dict1 and dict2

# Python 3.9 add the dict union operator (|) it will return a new dict containing items from the left and right dicts.
# in case of duplicated keys, the right side wins

dict4 = dict2 | dict1

print(dict4)