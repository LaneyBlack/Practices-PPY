"""
    Lab06 - localization
"""
print("-----------------Example1-----------------")
x = 5


def show1(a):
    x = a
    print(x)


show1(2)
print(x)

print("-----------------Example2-----------------")
y=4
def show2(b):
    global y
    y = b
    print(y)

show2(8)
print(y)

print("-----------------Example3-----------------")
def func1():
    a = 5
    print(a)
    def func2():
        nonlocal a
        a = 10
    func2()
    print(a)

func1()
