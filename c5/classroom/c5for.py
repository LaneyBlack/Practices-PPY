print("-----------------Fast fors-----------------")
# Interesting declarations
s1 = {a: a + 1 for a in [1, 2, 3]}
print(s1)
print([2 * x for x in range(1, 6)])
# Code table of ASCII
print([(x, ord(x)) for x in "ABCDEFGHIJKLMNOP"])
# List of empty lists
print([[] for x in range(10)])
# If in the print
print([x for x in range(20) if not (x % 3) or not (x % 5)])
print("-----------------Complicated fors-----------------")
# Postac rozszerzona
print([(x, y) for x in range(1, 5)
       for y in range(4, 0, -1)])

print([(x, y) for x in range(5)
       for y in range(6, 3, -1)
       if x < y])

# dict with even and odd numbers
print([(x,y) for x in range(5)
              for y in range(6,1,-1)
              if not (x%2) or y%2])

print([(x,y) for x in range(5) if not (x%2)
              for y in range(6,1,-1)
              if y%2])