

for num_bottles in range(100, 0, -1):
    print(f"{num_bottles} bottles of beer on the wall.")
    print(f"{num_bottles} bottles of beer")
    if(num_bottles == 1):
        print(f"Take one down, pass it around, no more bottle of beer on the wall")
    else: 
        print(f"Take one down, pass it around, {num_bottles - 1} bottles of beer on the wall")
    print("*" * 75)
