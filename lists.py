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


#  the sort method overrides the content of the list, it doesn't return anything
list_nums = [1 -5, 5, 12, 10, 14, 4, 2, 3]
list_nums.sort()

# reverse the values of the list, like sort reverse overrides the content of the list and doesn't return anything
list_nums.reverse()

# Count return number of occurrences in the list, if not found returns 0
langs = ["C", "Javascript", "Python", "C#"]
langs.count("C")

# Comparing list with ==  vs is keyword
nums1 = [1, 2, 3]
nums2 = nums1
#  like javascript python work with references which they call id, nums1 and nums2 share the same reference
#  so nums2 == nums1 is True and nums2 is nums1 also True

nums3 = [1, 2, 3]
# this one is tricky, nums1 == nums3 is True because == only verifies the values of the lists
# nums3 is nums1 gives False, because they do not share the same reference
# once you declare a list by this [], it automaticaly creates a new reference in memory
import copy
list = ["Apple","Banana", "Tomatoes"]
list1 = list.copy()

nested_list = ["Hello", 1, "Bro", "Sis", ["Are", "You", "Mad"]]
