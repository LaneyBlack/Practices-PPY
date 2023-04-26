"""
    Zbiory (Sets)
"""
print("1---")
zb1 = {3, 5, 7}
zb2 = {4, 6, 8, 2, 3}
print(zb1.union(zb2))
print(zb1 | zb2)
print("2---")
print(zb1.intersection(zb2))
print(zb1 & zb2)
print("3---")
print(zb1.difference(zb2))
print(zb1-zb2)
print(zb2-zb1)
print("4---")
print(zb1.symmetric_difference(zb2))
print(zb1^zb2)
print("5---")
zb2.remove(4)
print(zb2)
zb2.discard(4) # not throws exception
print(zb2)
print("6---")
zb1.clear()
print(zb1)