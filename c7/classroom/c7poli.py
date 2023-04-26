class Animal:
    family = "Animal"
    types = {}

    # Class initialisation
    def __init__(self, type, age, max_speed):
        self.type = type
        self.age = age
        self.max_speed = max_speed
        if type in Animal.types:
            Animal.types[type] += 1
        else:
            Animal.types[type] = 1

    def count_path(self, time):
        print(time * self.max_speed)

    @staticmethod
    def print_types():
        print(Animal.types)

    # Special methods:
    def __str__(self):
        return self.type + " is " + str(self.age) + " years old, has max speed of " + str(self.max_speed) + " km/h."


class Bird(Animal):
    def __init__(self, type, age, max_speed, fly_speed, place):
        super().__init__(type, age, max_speed)
        self.fly_speed = fly_speed
        self.place = place

    def move(self):
        if self.place == "cage":
            self.place = "open"
        else:
            self.place = "cage"


a = Animal("Lion", 3, 10)
print(a)
p = Bird("Penguin", 2, 3, 0, "open")
print(p)
print(p.place)
p.move()
print(p.place)
p.move()
print(p.place)
