# * tells python to collect all arguments into a tuple

# def average(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total / len(args)

# def count_arguments(*args):
#     print(f"you passed {len(args)} arguments")

def silly(first, second, *others):
    print(f"first is {first}")
    print(f"second is {second}")
    print(f"others are {others}")
