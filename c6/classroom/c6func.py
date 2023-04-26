"""
    Lab06 - Functions
"""

print("-----------------Example1-----------------")


# Just a function
def show(a, b):
    print(a, b, sep="")


def add(a, b):
    return a + b


show(5, 8)
c = add(4, 6)
print(c)

print("-----------------Example2-----------------")


# One function in another
def func1(a):
    print(a)

    def func2():
        print(a * 2)

    func2()


func1(4)

print("-----------------Example3-----------------")


# Alias for a function
def calc(a, b):
    print(a * b)


test = calc
test(2, 6)


print("-----------------Example4-----------------")
a = 10
if a < 5:
    def func():
        print("Lower than 5")
else:
    def func():
        print ("Higher than 5")
func()
