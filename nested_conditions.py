temp = 25
unit = "celsius"

if unit == "celsius":
    if temp <= 10:
        print("It's cold out there! :( ")
    elif temp <= 20:
        print("The weather is good! GO OUTSIDE")
    else:
        print("The weather is too hot, stay at home!")
else:
    print("SORRY, I don't know fahrenheit")


# More nested python
    
fav_color = "beige"
fav_movie = "memento"
fav_series = "true detective"
fav_food = "pasta"

if fav_color == "beige":
    print("My favorite color is beige")
    if fav_movie == "memento":
        print("My favorite movie is Memento")
        if fav_series == "true detective":
            print("My favorite series is True Detective (season 1 precisely)")
            if fav_food == "pasta":
                print("My favorite dish is pasta")



