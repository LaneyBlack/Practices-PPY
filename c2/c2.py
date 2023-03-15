# Declaration
x = 5
print(x)
x = 5 + 20
print(x)

# Strings
x = "Text"  # + 1 # throws exception
print(x)

# Many variables declaration
a, b, c = 1, "Wow", 4
print(c)
k = (1, 5, 7)
(x, y, z) = k
print(y)

# Variable deleting
print(id(x))
del x
# print (x) # throws exception

print("-------------------------------------------Types-------------------------------------------")
# Variable types
i = 5
f = 3.45
z = 3 + 5j
print(i, f, z)
print(type(i), type(f), type(z))  # Output: <class 'int'> <class 'float'> <class 'complex'>

# Number formats
(o, sz, b, e) = (0o45, 0x4b, 0b10110, 5e5)
print(o, sz, b, e)

# Strings
print("Czerwony" + " stoliczek")
print("Czerwony" " stoliczek")
print('Mot' 'or')


print("-------------------------------------------Strings-------------------------------------------")
# From number to String
s = "Age " + str(10)
print(s)
print(s.replace("A", "Ca").replace(" ", "-"))
print(s.upper())
print(s.lower())
# From String to number
a = "5"
print(int(a) + 10)

b = 7
print(a + repr(b))
print(a + str(b))

print("-------------------------------------------Operators-------------------------------------------")
(x,y) = (True, False)
print(x and y, x or y, not x , not y, x and not y, sep=" - ")
(x,y) = (21, 5)
print((x < y), (x>y), x<=y, x>=y, x==y, x!=y, sep=" - ")
print((x/y), (x*y), x%y, x-y, x+y, x**y, sep=" - ")
