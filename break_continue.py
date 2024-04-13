# for letter in "supercalifragilisticexpialidocious":
#     if letter == "c":
#         break
#     print(letter)

# message = input("please say hi: ")
# while True:
#     if message == "hi":
#         break
#     message = input("please say hi: ")
# print("THANK YOU FOR SAYING hi")

# for char in "FATCAT":
#     if char == 'A':
#         continue
#     print(char)

for letter in "supercalifragilisticexpialidocious":
    if letter in "aieou":
        continue
    print(letter)