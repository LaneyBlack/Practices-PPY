"""
    Lab06 argument args
"""

print("-----------------Example1-----------------")


def show1(a, b, c):
    print(a, b, c)


show1(1, 2, 3)
show1(a=3, c=2, b=1)
print("-----------------Example2-----------------")


def show2(a, b=4, c=5):
    print(a, b, c)


show2(1, 2, 3)
show2(1, 2)
show2(1)
show2(1, c=6)

print("-----------------Example3-----------------")


def show3(*arg):
    print(arg)


show3(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

print("-----------------Example4-----------------")


def show4(**arg):
    print(arg)


show4(a=1, b=2, c=3, d=4)

print("-----------------Example5-----------------")


def show5(a, b, c=3, *args, **kwargs):
    print(a, b, args, kwargs, sep="->")


show5(1, 2)
show5(1, 2, 3, 4, x=1, y=2)

print("-----------------Example6-----------------")


def show6(a, b, *args, c):
    print(a, b, args, c,sep="->")


show6(1, 2, 3, 4, 5, c=6)
