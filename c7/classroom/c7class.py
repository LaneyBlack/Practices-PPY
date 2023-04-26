print("--------------------ClassDefinition--------------------")

class Animal:
    family = "Animal"
    # Class initialisation
    def __init__(self, type, age):
        self.type = type
        self.age = age

    def print_type(self):
        print("Penguin")


a = Animal("lion", 5)
b = Animal("python", 2)

print(a)
print(b)
print(a == b)
print(a.type, a.age)
b.print_type()

print("Definitions out of class:")
b.length = 9
print(b.type, b.age, b.length)

print("Printing same variables of dif classes:")
print(a.family, b.family)
print(Animal.family)

print("Special attributes:")
print(a.__dict__)
print(b.__dict__)
print("Class documentation:")
print(Animal.__doc__)
print(a.__doc__)