fav_artists = ["Sia", "The weeknd", "Lana del rey", "Queen", "Arctic monkeys", "Coldplay", "Dua lipa", "Daft punk" ,"Cigarettes after sex", "Aimer", "Eden"]
fav_songs = {"weeknd": "Less than zero", "Lana": "Born to die", "Queen": "Under pressure", "Arctic Monkeys": "505", "Sia": "Breathe me", "CAS": "Cry", "Aimer": "Black bird"}

print("Your favorite artists are : ")
for artist in fav_artists:
    print(f"- {artist}")

for k,v in fav_songs.items():
    print(f"Your favorite {k} song is '{v}'")