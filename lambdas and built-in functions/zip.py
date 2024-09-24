midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ["dan", "kate", "ibrahim"]

# final_grades = {'dan': 98, 'kate': 91, 'ibrahim': 78}
highest_grades = dict(zip(students, (max(pair) for pair in zip(midterms, finals))))
# highest_grades = {pair[0]: max(pair[1], pair[2]) for pair in zip(students, midterms, finals)}

average_grades = dict(zip(students, (sum(pair) // len(pair) for pair in zip(midterms, finals))))
# average_grades = {pair[0]: (pair[1] + pair[2]) // 2 for pair in zip(students, midterms, finals)}

print("Highest grades of this class: ", highest_grades)
print("Average grades of this class: ", average_grades)