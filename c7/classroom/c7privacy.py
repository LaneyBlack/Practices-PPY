class Animal:
    family = "Animal"
    types = {}

    # Class initialisation
    def __init__(self, type, age, max_speed, health):
        self.type = type
        self.age = age
        self.max_speed = max_speed
        self.health = health
        if type in Animal.types:
            Animal.types[type] += 1
        else:
            Animal.types[type] = 1

    def _check_health(self):
        if self.health == 1:
            return 1
        else:
            return 0

    def count_path(self, time):
        print(time * self.max_speed)

    @staticmethod
    def print_types():
        print(Animal.types)

    # Special methods:
    def __str__(self):
        return self.type + " is " + str(self.age) + " years old, has max speed of " + str(self.max_speed) + " km/h."


class Bird(Animal):
    def __init__(self, type, age, max_speed, health, fly_speed, place):
        super().__init__(type, age, max_speed, health)
        self.fly_speed = fly_speed
        self.place = place

    def move(self):
        if self.place == "cage" and self._check_health():
            self.place = "open"
        else:
            self.place = "cage"

    def count_path(self, time):
        if self.fly_speed == 0:
            print(time * self.max_speed)
        else:
            print(time * self.fly_speed)


p = Bird("Penguin", 2, 3, 1, 0, "open")
b = Bird("Eagle", 2, 2, 0, 15, "cage")

p.count_path(2)
b.count_path(2)

#Private methods
print(p.place)
p.move()
print(p.place)
print(b.place)
b.move()
print(b.place)
