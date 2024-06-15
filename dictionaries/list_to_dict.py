person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
# method 1 
answer1 = {val[0]: val[1] for val in person}
print("Answer with method 1: ", answer1)

# method 2
answer2 = {k:v for k,v in person}
print("Answer with method 2: ",answer2)

# method 3
answer3 = dict(person)
print("Answer with method 3: ", answer3)