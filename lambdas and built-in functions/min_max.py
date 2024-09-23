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
