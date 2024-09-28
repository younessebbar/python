midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ["dan", "kate", "ibrahim"]

# final_grades = {'dan': 98, 'kate': 91, 'ibrahim': 78}
# highest_grades = dict(zip(students, (max(pair) for pair in zip(midterms, finals))))
# highest_grades = {pair[0]: max(pair[1], pair[2]) for pair in zip(students, midterms, finals)}

# average_grades = dict(zip(students, (sum(pair) // len(pair) for pair in zip(midterms, finals))))
# average_grades = {pair[0]: (pair[1] + pair[2]) // 2 for pair in zip(students, midterms, finals)}

# using built-in functions
highest_grades = zip(students, map(lambda pair: max(pair), zip(midterms, finals)))
average_grades = zip(students, map(lambda pair: sum(pair) // 2, zip(midterms, finals)))


print("Highest grades of this class: ", dict(highest_grades))
print("Average grades of this class: ", dict(average_grades))

# interleave function
def interleave(str1, str2):
    """Takes 2 strings and concat each character from str1 with str2, taking in consideration their indices"""
    return ''.join(''.join(s) for s in zip(str1, str2))

interleave('hi','ha')    # 'hhia'
interleave('aaa', 'zzz')  # 'azazaz'
interleave('lzr','iad') #  'lizard'