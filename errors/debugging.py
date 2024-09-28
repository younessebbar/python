import pdb

first ='First'
second ='Second'
pdb.set_trace()
result = first + ' ' + second
third = 'Third'
result += ' ' + third  
print(result)

# Common PDB commands
# l (list)
# n (next line)
# p (print)
# c (continue - finishes debugging)

def add_number(a, b, c, d):
    import pdb; pdb.set_trace()
    return a + b + c + d

add_number(5, 6, 7, 8)
