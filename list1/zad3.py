#Ex3 - 3pkt
symbol = "* "
a = 4 # width (x)
b = 3 # height (y)
for i in range(b):
    if i==0 or i==b-1:
        print(symbol*a)
    else:
        print(symbol, "  "*(a-3), symbol)
print("Area of this square is: ", a*b)
print("Perimeter of this square is: ", (a+b)*2)