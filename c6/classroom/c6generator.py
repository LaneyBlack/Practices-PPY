"""
    Lab06 - Generator
"""


def generator(a):
    for i in range(a):
        yield i + 1


for i in generator(4):
    print(i, end=" ")
print()

gen = generator(6)
while (x:=next(gen, None)):
    print(x, end=" ")
