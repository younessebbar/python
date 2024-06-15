test_score = {
    "Khadija": 100,
    "Younes": 87,
    "Nadia": 89,
    "Ayoub": 98,
    "Aniss": 45,
    "Hamza": 83,
    "Kaoutar": 67,
    "Chaimaa": 78,
    "Fariss": 23,
    "Nidal": 12,
    "Kenza": 48
}

# dict.keys()
# dict.values()
# dict.items()

# for student in test_score.keys():
#     print(student)

# total = 0
# for score in test_score.values():
#     total += score

# print(total / len(test_score))

# for key in test_score.keys():
#     print(key, test_score[key])

max_score = 0
best_student = ""
for student, score in test_score.items():
   if score > max_score:
      max_score = score
      best_student = student

print(f"{best_student} got the highest score of {max_score}")