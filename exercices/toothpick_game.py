print("*" * 20)
print("WELCOME TO THE GAME")
print("*" * 20)
player1_name = input("Enter player 1's name: ")
player2_name = input("Enter player 2's name: ")
num_left = 13
current_player = player1_name

while True:
    print("| " * num_left)
    print(f"There are {num_left} toothpicks left")
    choice = int(input(f"How many toothpicks do you take, {current_player} ? "))
    while choice != 1 and choice != 2 and choice != 3:
        choice = int(input("You can only take 1, 2 or 3: "))
    num_left -= choice
    if num_left == 0:
        print(f"{current_player} wins !!")
        break
    if current_player == player1_name:
        current_player = player2_name
    else:
        current_player = player1_name

print("GAME OVER!")



# while num_left > 0:
#     print("|" * num_left)
#     print(f"There are {num_left} left")
#     p1_num = int(input(f"How many do you take, {player1_name} ? "))
#     num_left -= p1_num
#     winner = player1_name
#     if(num_left > 0):
#          print("|" * num_left)
#          print(f"There are {num_left} left")
#          p2_num = int(input(f"How many do you take, {player2_name} ? "))
#          num_left -= p2_num
#          winner = player2_name

# print(f"{winner} wins !!!")
# print("GAME OVER!")

   


