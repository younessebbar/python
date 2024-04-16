tasks = ["Trash", "Dishes", "Laundy", "Dinner"]

# append is the equivalent of push in JS => ["Trash", "Dishes", "Laundy", "Dinner", "Learn python"]
tasks.append("Learn python")

# extend accepts an iterable =>  ["Trash", "Dishes", "Laundy", "Dinner", "Learn python","Late night workout", "Sleep"]
tasks.extend(["Late night workout", "Sleep"])

nums = [7, 5, 6]
nums.insert(2, "Younes")

print(nums)
print(tasks)

# Slice method on lists is the same as strings => syntax is list[start:stop:step] doesn't include the stop
# You can insert into an existing list a new values using the slice method
print(tasks[5:])
nums[1:3] = ["well", "hello", "there", "mate"]
print(nums)

# for removing from the list there are 4 methods clear, remove, pop, popitems
# pop removes the last element in the list and returns it, pop can take an index pop(idx) to remove from a specific index
nums.pop()
nums.pop(1)

# remove used to delete a specific entry in the list, returns NONE
tasks.remove("well")

# popitems


nums.clear() 
print(nums)

# nums is empty
