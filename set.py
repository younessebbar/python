evens = {2, 4, 6, 8, 10, 12, 14}
odds = {1, 3, 5, 7, 9}

# add method
evens.add(28)
odds.add(21)
# remove method
evens.remove(2)
odds.remove(3)
# discard method, like remove the only difference is that it doesn't throw an error when you give a value that doesn't exist in the set
evens.discard(56)

# intersection left & right -> returns a new set with common values between the two sets
webdev = {"html", "css", "js", "python", "SQL"}
dataScience = {"R", "python", "SQL"}
print(webdev & dataScience)
# {'SQL', 'python'} printed

# union left | right ->  returns new set with members from left and right
print(webdev | dataScience) 
# {"R", "python", "SQL", "html","css","js"} printed

# difference left - right -> returns new set with members from left not in right
print(webdev - dataScience)
# {"html","css","js"}




