fav_artists = ["Sia", "The weeknd", "Lana del rey", "Queen", "Arctic monkeys", "Coldplay", "Dua lipa", "Daft punk" ,"Cigarettes after sex", "Aimer", "Eden"]
fav_songs = {
    "weeknd": ["Less than zero", "I feel it coming", "Save your tears"],
    "Lana": ["Born to die", "Margaret", "Radio"],
    "Queen": ["Under pressure", "Bohemian Rhapsody"],
    "Arctic Monkeys": ["505", "Do i wanna know", "Wanna be yours"],
    "Sia": ["Breathe me", "Still Here", "Wild Ones"],
    "CAS": ["Cry", "K.", "Sunsetz"],
    "Aimer": ["Black bird", "Blind To you", "Ref:rain"],
    "Dua Lipa": ["Be the one", "Don't start now", "Houdini"],
    "Coldplay": ["Clocks", "Yellow", "A sky full of stars"]
    }

# print("Your favorite artists are : ")
# for artist in fav_artists:
#     print(f"- {artist}")

for artist,songs in fav_songs.items():
    print(f"Your favorite {artist} songs are: ")
    for song in songs:
        print(f"- {song}")
