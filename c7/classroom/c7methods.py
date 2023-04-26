
class Animal:
    family = "Animal"
    types = {}
    # Class initialisation
    def __init__(self, type, age, max_speed):
        self.type = type
        self.age = age
        self.max_speed = max_speed
        if type in Animal.types:
            Animal.types[type] +=1
        else:
            Animal.types[type] = 1

    def count_path(self, time):
        print(time*self.max_speed)

    @staticmethod
    def print_types():
        print(Animal.types)

    def print_type(self):
        print("Penguin")

#-----------------------------------------------------------------------------------------------------------------------

Animal.print_types()
a = Animal("lis", 5, 10)
b = Animal("lis", 3, 10)
c = Animal("python", 2, 5)

a.count_path(10)
c.count_path(10)

Animal.print_types()