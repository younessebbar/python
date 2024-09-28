# Syntax error -> Occurs when python encounters incorrect syntax (something it doesn't parse)
# usually due to typos or not knowing python very well

# def first: # Syntax Error

None = 1 # Syntax Error

# return # Syntax Error

# Name Error -> Occurs when a variable is not defined, it hasn't been assigned
# Type Error -> Occurs when an operation or function is applied to the wrong type

len(5) # Type Error

"awesome" + [] #Type Error

# Index Error -> happens when you try to access an element in a list using an invalid index
nums = [1, 2, 3]
nums[4] # Index Error - list index out of range

# Value Error -> occurs when built-in operation or function receives an argument that has the right type but inappropriate value:
int("foo")

# Key Error -> this happens when dictionary doesn't have the specific key
d = {"name": "Younes", "age": 28}
d["ahah"]

# Attribute Error -> this happens when a variable doesn't have an attribute
"awesome".foo 
