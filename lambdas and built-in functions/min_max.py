names = ["Arya", "Dora", "Tim", "Samson", "Ollivander"]

print(f"Shortest name in the list is {min(names, key=lambda name: len(name))}")
print(f"Longest name in the list is {max(names, key=lambda name: len(name))}")

songs = [
    {"title": "Maps", "playcount": 102364},
    {"title": "Lucky", "playcount": 789450},
    {"title": "Phoenix", "playcount": 946413},
    {"title": "Cage", "playcount": 564965},
    {"title": "Wake Up", "playcount": 478945},
]

print("The least played song is",  min(songs, key=lambda song: song['playcount'])['title'])
print("The most played song is", max(songs, key=lambda song: song['playcount'])['title'])

def max_magnitude(nums):
    return max(abs(num) for num in nums)

max_magnitude([300, 20, -900]) #900
max_magnitude([10, 11, 12])   #12
max_magnitude([-5, -1, -89])  #89

def sum_even_values(*collection):
    return sum(num for num in collection if num % 2 == 0)

sum_even_values(1,2,3,4,5,6) # 12
sum_even_values(4,2,1,10) # 16
sum_even_values(1) # 0
