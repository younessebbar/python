# def laugh(intensity):
#     print("HA" * intensity)

# def divide(a, b):
#     return a / b

# print(divide(4, 100))

# def is_even(num):
#     return num % 2 == 0

def slugify(phrase, seperator = "_"):
    return phrase.strip().lower().replace(" ", seperator)

print(slugify("Hello world I LOVE You", "1"))

def get_total(price, qty = 1, tax = 0.02, discount = 0):
    subtotal = price * qty  * (1 - discount)
    print(subtotal * (1 + tax))

get_total(4.99, 5, 0.01, 0.5)
get_total(price= 4.99, qty= 5, tax= 0.01, discount= 0.5)
get_total(price= 4.99, discount= 0.5, qty= 5,tax= 0.01)
get_total(9.99)


# def count_vowels(phrase):
#     count = 0
#     for char in phrase:
#         if char in "aieou":
#             count += 1
#     return count

# def laugh(intensity = 5):
#     print("HA" * intensity)