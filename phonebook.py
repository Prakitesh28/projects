class phonebook:
    phone_directory = []

    def __init__(self, name, number):
        self.name = name
        self.number = number
        phonebook.phone_directory.append(self)

    def display(self):
        return self.name, self.number


p1 = phonebook("prakitesh", 1234567890)
p2 = phonebook("satyarth", 9876543210)

print(p1.display())
print(p2.display())