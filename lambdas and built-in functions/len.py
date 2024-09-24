class specialClass:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return self.data.__len__() // 2
    
# // gives the inter result of the divide operation

c1 = specialClass(["Hello"," Mother", "Father"])
c2 = specialClass([14, 45, 63, 78, 41])
print(len(c1))
print(len(c2))
