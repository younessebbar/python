emails = ["younes@gmail.com", "marwa@gmail.com", "aymane@gmail.com", "ayoub@gmail.com", "sara@gmail.com", "inas@gmail.com"]


# for char in "Hellow":
#     print(char)

# for email in emails:
#     print(email)

# idx = 0
# while idx < len(emails):
#     print(emails[idx])
#     idx += 1

lando_2021_results = [4, 3, 4, 5, 3, 4, 8, 10, 4, 10, 7, 10, 2, 5, 5, 5, 9,1]

# sum = 0
# for num in lando_2021_results:
#     sum += num
# avg = round(sum / len(lando_2021_results))


def average(nums):
    total = 0
    for num in nums:
        total += num
    return round(total / len(nums))

min = lando_2021_results[0]
for num in lando_2021_results:
    if num < min:
        min = num

print(min)