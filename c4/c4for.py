"""
    Lab04 - For
"""
print("Simple for")
print("1---")
listA = ["abc", [1,2,3]]
for i in listA:
    print(i)
print("2---")
for i in range(len(listA)):
    print(i)
print("3---")
for i in listA:
    print(i)
    for j in i:
        print(j)
print("Text formatting" ) #Python 2.7 - 3.x
print("1---")
for x in range(-10,11):
    print("%+i" % x, end=" ")
print()
print("2---")
for x in range(5,100,10):
    print("%3i%6o%5x" % (x,x,x)) # wyrownanie od prawej
print("3---")
for x in range(5,100,10):
    print("%-3i%#-6o%-5x" % (x,x,x)) # wyrownanie od lewej
print("4---")
for x in range(5,100,10):
    print("%#-3i%#-6o%#-5x" % (x,x,x)) # wyrownanie od lewej #prefix rzeczywusty
print("5---")
for x in range(5,100,10):
    print("%03i %04o %04x" % (x,x,x))
print("6---") #Python 3.x
for x in range(5,100,10):
    print("{} {} {}".format(x, oct(x), hex(x)))
