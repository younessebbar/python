list_nums = [2, 5, 8, 15, 45, 12]
print([n * 2 for n in list_nums])

friends = ["ross","chandler","phoebe","monica","joey","rachel"]

# uppercase the whole names
print([name.upper() for name in friends]) 
# uppercase only the first character
print([name[0].upper() + name[1:] for name in friends])

#  we can also transform given lists to some other primitif type
print([bool(val) for val in [0, '', [], 12]])
print([str(val) for val in [45, 21, 13, 10, 49]])

# we can also combine list comprehension with conditions
numbers = [14, 1, 15, 12, 13, 11, 18, 17, 19]
odds = [num for num in numbers if num % 2 != 0]
evens = [num for num in numbers if num % 2 == 0]
multiply_evens = [num * 2 if num % 2 == 0 else num for num in numbers]
print("odd numbers: ", odds)
print("even numbers: ", evens)
print("multiply evens by 2: ", multiply_evens)

# example to remove vowels from a string
with_vowels = "This is so much fun"
''.join(char for char in with_vowels if char not in "aieou")

# using LC for list intersection conditions
[num for num in [1, 2, 3, 4] if num in [3, 4, 5, 7]]
# returns numbers that exist on the two arrays

# NB val[::-1] the quickest way to reverse a string in python
[val[::-1].lower() for val in ["Younes","Yassine","Ayoub"]]

# Nested List comprehension
nested_list = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
# print values in nested list using LC (list comprehension)

[[print(val) for val in l] for l in nested_list]