dict1 = {"a": 1, "b": 2, "c": 3}
print(dict1)
# clear empties the dictionary
dict1.clear()
print(dict1)

# create new dictionaries syntax
user = dict(name= "younes", age=28)
print(user)

# this syntax create a new dictionary with keys  of the first argument and the values of the second argument
# first argument should always be an iterable whether a list, string, tuple, set and range method
new_dict = {}.fromkeys(["name", "age", "profile bio", "email", "score"], "null")
print(new_dict)

# get method gives you the corresponding value of the key passed, if it's not there it gives you None instead
print(user.get("age"))

# pop deletes the key value pair and returns only the value
age = user.pop("age")
print(age, user)

# popitem remove the last key,value pair and returns them as a tuple
deleted_item = user.popitem()
print(type(deleted_item), user)

# update doesn't remove things, it add key, value pairs if they don't exist and update the value of existing key pairs
first = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
second = {}

second.update(first)
print(second)
