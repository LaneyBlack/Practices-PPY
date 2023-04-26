"""
    Lab04 - While
"""
print("Simple while")
print("1---")
a = 0
while a < 5:
    a+=1
    print(a)
print("2---")

x={1, 2, 3, 4, 5}
while x:
    print(x.pop())
else:
    print("Zbior jest pusty")
print("3---")
x = 0
while x < 3:
    x+=1
    print(x)
    a = 1
    while a<5:
        a*=2
        print("a =", a)
print("4---")
